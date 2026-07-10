<div align="center">
  <h1>YOLO Orange Ball Detection</h1>
  <p>用于橙色球目标检测的 YOLO 训练与推理实验，包含数据集、模型权重和摄像头脚本。</p>

  <p>
    <a href="README.md">English</a>
    &middot;
    <a href="#快速开始">快速开始</a>
    &middot;
    <a href="#技术栈">技术栈</a>
  </p>

  <p>
    <img alt="Python: YOLO" src="https://img.shields.io/badge/Python-YOLO-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Ultralytics: training" src="https://img.shields.io/badge/Ultralytics-training-111111?style=for-the-badge" />
    <img alt="Vision: object detection" src="https://img.shields.io/badge/Vision-object%20detection-287866?style=for-the-badge" />
  </p>
</div>

<p align="center">
  <img src=".github/assets/readme-hero.svg" alt="YOLO Orange Ball Detection 项目概览图" width="100%" />
</p>

## 项目价值

颜色阈值检测很有用，但学习式检测更适合复杂背景。本仓库把橙色球数据集、训练脚本、导出权重和摄像头实验放在一起。

## 快速开始

```bash
git clone https://github.com/Ha22yX/Yolo-Orange-Ball-detection.git
cd Yolo-Orange-Ball-detection
pip install ultralytics opencv-python onnxruntime numpy pillow pyserial
python Tarining/scripts/webcam_detect.py --weights Tarining/runs/yolo11n-rpi-416/weights/best.pt --cam 0
```

目录名 `Tarining` 保持原样，因为现有路径依赖它。

## 核心功能

- 包含彩色和灰度版本的 YOLO 格式橙色球数据集。
- 提供训练、摄像头、视频、ONNX 导出和 ONNX 视频推理脚本。
- 包含当前实验使用的 YOLO 权重。
- 包含 ESP32-S3 摄像头串口实验，用于嵌入式采集测试。

## 技术栈

| Layer | Technology | Role |
| --- | --- | --- |
| 模型 | YOLO / Ultralytics | 训练和检测脚本。 |
| 推理 | OpenCV, ONNX Runtime | 摄像头/视频推理和导出模型测试。 |
| 数据 | YOLO dataset format | 图像、标签和 data.yaml 文件。 |
| 嵌入式 | ESP32-S3 camera | 串口图像实验。 |


## 项目说明

这是实验仓库，为复现实验保留了数据集和模型文件。后续如果扩展，建议把大模型和数据集移到 GitHub Releases 或外部存储。
