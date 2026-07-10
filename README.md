<div align="center">
  <h1>YOLO Orange Ball Detection</h1>
  <p>Training and inference experiments for detecting orange balls with YOLO models, datasets, and camera scripts.</p>

  <p>
    <a href="README.zh-CN.md">Chinese</a>
    &middot;
    <a href="#quickstart">Quickstart</a>
    &middot;
    <a href="#features">Features</a>
    &middot;
    <a href="#tech-stack">Tech Stack</a>
  </p>

  <p>
    <img alt="Python: YOLO" src="https://img.shields.io/badge/Python-YOLO-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Ultralytics: training" src="https://img.shields.io/badge/Ultralytics-training-111111?style=for-the-badge" />
    <img alt="Vision: object detection" src="https://img.shields.io/badge/Vision-object%20detection-287866?style=for-the-badge" />
  </p>
</div>

<p align="center">
  <img src=".github/assets/readme-hero.svg" alt="YOLO Orange Ball Detection overview image" width="100%" />
</p>

<p align="center">
  <img src="Tarining/runs/yolo11n-rpi-416/results.png" alt="YOLO training metrics" width="49%" />
  <img src="Tarining/runs/yolo11n-rpi-416/val_batch0_pred.jpg" alt="YOLO validation prediction examples" width="49%" />
</p>

## Overview

This repo keeps the learned-detector path for orange-ball detection in one place: datasets, training scripts, trained weights, validation outputs, ONNX export, and camera inference tools.

It complements the classical OpenCV detector by using YOLO when lighting, backgrounds, and viewpoints are too variable for simple color thresholds alone.

## Features

- YOLO-format datasets and trained model artifacts.
- Training, webcam inference, video inference, ONNX export, and ONNX runtime scripts.
- Validation images and training metrics preserved with the experiment run.
- ESP32-S3 camera serial sketch for embedded capture experiments.
- Clear path from dataset labeling to model testing on a live camera.

## How It Works

1. Prepare images and labels in YOLO format.
2. Train or reuse a small Ultralytics YOLO model.
3. Run live inference from webcam/video or exported ONNX runtime.
4. Compare validation predictions and metrics before using a weight in robotics experiments.

## Quickstart

Run the project locally with the commands below.

```bash
git clone https://github.com/Ha22yX/Yolo-Orange-Ball-detection.git
cd Yolo-Orange-Ball-detection
pip install ultralytics opencv-python onnxruntime numpy pillow pyserial
python Tarining/scripts/webcam_detect.py --weights Tarining/runs/yolo11n-rpi-416/weights/best.pt --cam 0
```

The folder name `Tarining` is preserved because existing experiment paths depend on it.

## Configuration

| Item | Purpose |
| --- | --- |
| Weights | Point scripts to `best.pt`, `yolo11n.pt`, or exported ONNX files. |
| Camera index | Use the script option or OpenCV device index that matches your camera. |
| Dataset paths | Keep `data.yaml`, images, and labels aligned before training. |
| Embedded capture | Use the Arduino sketch only after confirming serial baud and frame format. |

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
| Model | YOLO / Ultralytics | Training and detection pipeline. |
| Inference | OpenCV, ONNX Runtime | Camera/video inference and exported model tests. |
| Data | YOLO dataset format | Images, labels, and `data.yaml` files. |
| Embedded | ESP32-S3 camera | Serial capture experiments. |

## Project Layout

```text
Tarining/scripts/              training, inference, export, and serial tools
Tarining/Dataset/              YOLO-format dataset examples
Tarining/runs/yolo11n-rpi-416/ experiment outputs and weights
arduino/                       ESP32-S3 camera serial sketch
.github/assets/                README overview asset
```

## Status

Research/experiment repository. Model artifacts are included for reproducibility; large future datasets should move to Releases or external storage.

## Related Projects

- [OrangeBall-Detection-with-OpenCV](https://github.com/Ha22yX/OrangeBall-Detection-with-OpenCV) - classical live-tunable detector for the same object class.

## License

No project-wide open-source license has been declared yet.
