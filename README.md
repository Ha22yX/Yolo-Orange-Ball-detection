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

## Why This Exists

Color thresholding is useful, but learned detection can handle more background variation. This repo keeps the orange-ball dataset, training scripts, exported weights, and camera experiments together.

## Quickstart

```bash
git clone https://github.com/Ha22yX/Yolo-Orange-Ball-detection.git
cd Yolo-Orange-Ball-detection
pip install ultralytics opencv-python onnxruntime numpy pillow pyserial
python Tarining/scripts/webcam_detect.py --weights Tarining/runs/yolo11n-rpi-416/weights/best.pt --cam 0
```

The folder name `Tarining` is kept as-is because existing paths depend on it.

## Features

- YOLO-format color and grayscale orange-ball datasets.
- Training, webcam, video, ONNX export, and ONNX video inference scripts.
- Included YOLO weights for reproducing current experiments.
- ESP32-S3 camera serial experiment for embedded capture tests.

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
| Model | YOLO / Ultralytics | Training and detection scripts. |
| Inference | OpenCV, ONNX Runtime | Camera/video inference and exported model tests. |
| Data | YOLO dataset format | Images, labels, and data.yaml files. |
| Embedded | ESP32-S3 camera | Serial frame experiments. |


## Project Notes

This is an experiment repository with datasets and model artifacts checked in for reproducibility. For a larger release, move heavy weights/datasets to GitHub Releases or external storage.
