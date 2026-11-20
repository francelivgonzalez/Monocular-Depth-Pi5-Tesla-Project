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

## Tech Stack

- **Hardware:** Raspberry Pi 5
- **Software:** Python, OpenCV, LiteRT, NumPy
- **Model:** MiDaS v2.1 Small
