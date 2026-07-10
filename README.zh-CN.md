<div align="center">
  <h1>YOLO Orange Ball Detection</h1>
  <p>一个橙色球体检测实验仓库，包含 YOLO 数据集、训练脚本、权重、ONNX 导出和摄像头推理工具。</p>

  <p>
    <a href="README.md">English</a>
    &middot;
    <a href="#快速开始">快速开始</a>
    &middot;
    <a href="#核心能力">核心能力</a>
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

<p align="center">
  <img src="Tarining/runs/yolo11n-rpi-416/results.png" alt="YOLO 训练指标" width="49%" />
  <img src="Tarining/runs/yolo11n-rpi-416/val_batch0_pred.jpg" alt="YOLO 验证预测示例" width="49%" />
</p>

## 项目概览

这个仓库把橙色球体的学习式检测路线放在一起：数据集、训练脚本、已训练权重、验证输出、ONNX 导出和摄像头推理工具。

它与传统 OpenCV 检测器互补：当光照、背景和视角变化较大，简单颜色阈值不够稳定时，可以使用 YOLO。

## 核心能力

- YOLO 格式数据集和已训练模型文件。
- 训练、摄像头推理、视频推理、ONNX 导出和 ONNX Runtime 脚本。
- 保留验证图片和训练指标，便于复现实验。
- ESP32-S3 摄像头串口草图，用于嵌入式采集实验。
- 从数据标注到实时模型测试的完整实验路径。

## 工作方式

1. 准备 YOLO 格式图片和标签。
2. 训练或复用一个轻量 Ultralytics YOLO 模型。
3. 用摄像头/视频或导出的 ONNX 模型运行推理。
4. 在机器人实验使用权重前，先对比验证预测和训练指标。

## 快速开始

可以用下面的命令在本地运行项目。

```bash
git clone https://github.com/Ha22yX/Yolo-Orange-Ball-detection.git
cd Yolo-Orange-Ball-detection
pip install ultralytics opencv-python onnxruntime numpy pillow pyserial
python Tarining/scripts/webcam_detect.py --weights Tarining/runs/yolo11n-rpi-416/weights/best.pt --cam 0
```

`Tarining` 文件夹名保留不改，因为已有实验路径依赖这个名称。

## 配置项

| 项目 | 作用 |
| --- | --- |
| 模型权重 | 把脚本指向 `best.pt`、`yolo11n.pt` 或导出的 ONNX 文件。 |
| 摄像头编号 | 使用脚本参数或 OpenCV 设备编号匹配本机摄像头。 |
| 数据集路径 | 训练前确保 `data.yaml`、图片和标签一致。 |
| 嵌入式采集 | 使用 Arduino 草图前先确认串口波特率和帧格式。 |

## 技术栈

| 层级 | 技术 | 作用 |
| --- | --- | --- |
| 模型 | YOLO / Ultralytics | 训练和检测流程。 |
| 推理 | OpenCV, ONNX Runtime | 摄像头/视频推理和导出模型测试。 |
| 数据 | YOLO dataset format | 图片、标签和 `data.yaml`。 |
| 嵌入式 | ESP32-S3 camera | 串口采集实验。 |

## 项目结构

```text
Tarining/scripts/              训练、推理、导出和串口工具
Tarining/Dataset/              YOLO 格式数据集示例
Tarining/runs/yolo11n-rpi-416/ 实验输出和权重
arduino/                       ESP32-S3 摄像头串口草图
.github/assets/                README 概览图
```

## 项目状态

这是研究/实验仓库。模型文件保留在仓库中方便复现；未来更大的数据集建议迁移到 Releases 或外部存储。

## 相关项目

- [OrangeBall-Detection-with-OpenCV](https://github.com/Ha22yX/OrangeBall-Detection-with-OpenCV) - 同一目标的传统视觉检测器。

## 许可证

当前仓库尚未声明项目级开源许可证；公开复用或分发前建议先补充 License。
