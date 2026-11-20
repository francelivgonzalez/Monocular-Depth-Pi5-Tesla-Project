# Monocular-Depth-Pi5-Tesla-Project
> Turning 2D camera frames into real-time depth maps on edge hardware-with OpenCV, LiteRT, and MiDaS v2.1 on a Raspberry Pi 5.

A vision-only monocular depth estimation pipeline on a Raspberry Pi 5 using OpenCV and LiteRT (MiDaS v2.1 Small) to extract 3D spatial awareness from a single camera without radar or LiDAR.

## What This Project Does

Autonomous perception systems need to understand distance and layout in a scene, even from a single camera feed. **Monocular depth estimation** predicts relative depth from 2D images using a trained neural network.

This project runs a lightweight edge inference pipeline on a Raspberry Pi 5 to turn live or recorded camera frames into depth visualizations:
1. **Frame Capture & Preprocessing:** Capturing frames via OpenCV and normalizing tensors for model input.
2. **Edge Inference:** Running MiDaS v2.1 Small through LiteRT on embedded hardware.
3. **Depth Visualization:** Post-processing predicted depth maps with colormap rendering.

## What I'm Focusing On

- **Vision-Only Spatial Awareness:** Exploring how depth cues can be estimated purely from camera pixels without radar or LiDAR.
- **Edge Inference Performance:** Running MiDaS v2.1 Small with LiteRT on a Raspberry Pi 5 to keep latency low on resource-constrained hardware.
- **Preprocessing & Colormap Pipeline:** Moving smoothly from frame capture and tensor normalization to inference and colormap output.
- **First-Principles Camera Thinking:** Using this repo as a hands-on sandbox to practice end-to-end camera-to-perception reasoning.

## How the Pipeline Is Set Up

- **Hardware Target:** Raspberry Pi 5 running a single-camera vision pipeline.
- **Capture & Preprocessing (OpenCV + NumPy):** Reading frames, resizing/formatting inputs, and normalizing tensors for inference.
- **Inference Runtime (LiteRT):** Executing the MiDaS v2.1 Small model efficiently on edge hardware.
- **Post-Processing:** Mapping raw depth predictions into human-readable colormap visualizations.
- **Modular Structure & Reproducibility:** Separating the pipeline into `src/` modules with a clean `depth.py` entry point, pinned dependencies in `requirements.txt`, `.gitignore`, and `samples/` / `outputs/` for quick verification.

## How to Run

1. Install dependencies from `requirements.txt` in your Python environment on the Raspberry Pi 5:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your MiDaS v2.1 Small `.tflite` model under `models/` and run the entry script:
   ```bash
   python depth.py
   ```

## Tech Stack

- **Hardware:** Raspberry Pi 5
- **Software:** Python, OpenCV, LiteRT, NumPy
- **Model:** MiDaS v2.1 Small

## Repository Layout

```text
Monocular-Depth-Pi5-Tesla-Project/
├── README.md
├── requirements.txt          # Pin OpenCV, NumPy, and LiteRT/TFLite runtime dependencies
├── .gitignore                # Ignore __pycache__, virtual envs, temp frames, or large model weights if external
├── src/
│   ├── __init__.py
│   ├── capture.py            # Camera / video / image frame input handling via OpenCV
│   ├── preprocess.py         # Resize, color format conversion, and tensor normalization
│   ├── infer.py              # LiteRT / TFLite interpreter setup and MiDaS v2.1 Small execution
│   └── postprocess.py        # Depth normalization, colormap rendering, and FPS/latency overlay
├── models/                   # MiDaS v2.1 Small (.tflite) model file or download/setup notes
├── samples/                  # Sample input image(s) or short test clip for quick verification
├── outputs/                  # Example side-by-side RGB + depth colormap renders (keep small/curated)
└── depth.py                  # Clean CLI entry point wiring capture -> preprocess -> infer -> postprocess
```
