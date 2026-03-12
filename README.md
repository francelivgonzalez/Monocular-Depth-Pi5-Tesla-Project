# Monocular-Depth-Pi5-Tesla-Project
_PERSONAL PROJECT_
Monocular depth estimation Raspberry Pi using TFlite and OpenCV. Demonstrates vision-only inference pipeline for autonomous systems with real-time performance on edge hardware. Implements MiDaS v2.1 with custom ISP preprocessing and colormap visualization.

VISION-ONLY MONOCULAR DEPTH ESTIMATION


OVERVIEW

I built this project as a technical sandbox to prepare for my Camera Systems Development interview at Tesla. My goal was to apply first principles thinking to autonomous vision: extracting 3D spatial awareness from a 2D monocular camera without relying on radar or LiDAR. 

This repository demonstrates a complete edge inference pipeline, running a lightweight neural network (MiDaS v2.1) on a Raspberry Pi 5 to generate real-time depth maps.


CORE COMPETENCIES DEMONSTRATED
1. Vision-Only Philosophy: Proving that spatial data can be derived purely from pixel data using ML, aligning with a radar-less approach.
2. Edge Inference: Deploying a model using LiteRT for high-throughput performance on resource-constrained embedded hardware.
3. ISP Pipeline Architecture: Building a custom image processing pipeline, from raw frame capture via OpenCV, tensor normalization, inference execution, to post-processing with colormap visualizations.


TECH STACK
- Hardware: Raspberry Pi 5
- Software: Python, OpenCV, LiteRT, NumPy
- Model: MiDaS v2.1 Small
