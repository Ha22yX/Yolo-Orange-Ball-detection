<div align="center">
  <h1>YOLO Orange Ball Detection</h1>
  <p>Training and inference experiments for detecting orange balls with YOLO models, datasets, and camera scripts.</p>

  <p>
    <a href="README.zh-CN.md">Chinese</a>
    &middot;
    <a href="#quickstart">Quickstart</a>
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

## Why This Exists

Color-based detection is useful, but learned detectors handle more variation in lighting, background, and camera angle. This repo keeps the dataset, training scripts, model weights, and inference tools together for orange-ball detection experiments.

## Workflow

- Prepare YOLO-format color or grayscale datasets.
- Train a small YOLO model with Ultralytics scripts.
- Run webcam/video/dataset inference with trained weights.
- Export to ONNX for lighter runtime experiments.
- Use ESP32-S3 camera serial scripts for embedded capture tests.

## Features

- YOLO-format datasets and trained weights.
- Training, webcam, video, ONNX export, and ONNX inference scripts.
- Validation metrics and prediction images kept with the experiment run.
- ESP32-S3 camera serial experiment for hardware-side capture.

## Quickstart

```bash
git clone https://github.com/Ha22yX/Yolo-Orange-Ball-detection.git
cd Yolo-Orange-Ball-detection
pip install ultralytics opencv-python onnxruntime numpy pillow pyserial
python Tarining/scripts/webcam_detect.py --weights Tarining/runs/yolo11n-rpi-416/weights/best.pt --cam 0
```

The folder name `Tarining` is kept as-is because existing experiment paths depend on it.

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
| Model | YOLO / Ultralytics | Training and detection scripts. |
| Inference | OpenCV, ONNX Runtime | Camera/video inference and exported model tests. |
| Data | YOLO dataset format | Images, labels, and data.yaml files. |
| Embedded | ESP32-S3 camera | Serial frame experiments. |

## Project Map

```text
Tarining/scripts/              training, inference, export, and serial tools
Tarining/yolo-data/            YOLO-format dataset
Tarining/runs/yolo11n-rpi-416/ experiment outputs and weights
arduino/                       ESP32-S3 camera serial sketch
```

## Notes

Datasets and model artifacts are kept in the repository for reproducibility. Large future datasets should move to Releases or external storage.
