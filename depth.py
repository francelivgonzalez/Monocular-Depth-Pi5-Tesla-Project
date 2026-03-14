import cv2
import numpy as np
import tensorflow as tf
import time


class DepthEstimator:
    def __init__(self, model_path="midas_v2.1_small.tflite"):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.input_height = self.input_details[0]["shape"][1]
        self.input_width = self.input_details[0]["shape"][2]

    def estimate_depth(self, frame):
        # Convert BGR to RGB since many vision models expect RGB input
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize to model input size
        img_resized = cv2.resize(frame_rgb, (self.input_width, self.input_height))

        # Normalize image
        img_normalized = img_resized.astype(np.float32) / 255.0

        # Add batch dimension
        input_data = np.expand_dims(img_normalized, axis=0)

        # Run inference
        self.interpreter.set_tensor(self.input_details[0]["index"], input_data)
        self.interpreter.invoke()

        # Get output depth map
        depth_map = self.interpreter.get_tensor(self.output_details[0]["index"])
        depth_map = np.squeeze(depth_map)

        # Normalize for visualization only
        depth_min = depth_map.min()
        depth_max = depth_map.max()

        if depth_max - depth_min > 1e-6:
            depth_normalized = (depth_map - depth_min) / (depth_max - depth_min)
        else:
            depth_normalized = np.zeros_like(depth_map, dtype=np.float32)

        depth_vis = (depth_normalized * 255).astype(np.uint8)
        depth_colored = cv2.applyColorMap(depth_vis, cv2.COLORMAP_TURBO)

        return depth_colored, depth_map


def main():
    estimator = DepthEstimator("midas_v2.1_small.tflite")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera.")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera.")
            break

        depth_vis, depth_raw = estimator.estimate_depth(frame)
        depth_resized = cv2.resize(depth_vis, (frame.shape[1], frame.shape[0]))

        current_time = time.time()
        fps = 1.0 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        combined = np.hstack([frame, depth_resized])
        cv2.imshow("RGB | Depth Map", combined)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
