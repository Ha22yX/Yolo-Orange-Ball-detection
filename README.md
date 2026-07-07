# YOLO Orange Ball Detection

Training and inference experiments for detecting orange balls with YOLO models.
The project includes datasets, trained model weights, validation outputs, and a
small ESP32-S3 camera serial experiment.

## Repository Layout

```text
Tarining/
  scripts/                 Training, export, webcam, video, and serial tools.
  yolo-data/               YOLO-format color dataset.
  yolo-data-gray/          YOLO-format grayscale dataset.
  runs/yolo11n-rpi-416/    Training results and exported weights.
  Dataset/                 Earlier dataset layout and test media.

arduino/
  esp32s3_cam_serial/      ESP32-S3 camera serial sketch.
```

Note: the folder name `Tarining` is kept as-is to avoid breaking existing paths.

## Common Scripts

- `Tarining/scripts/train_yolonano.py` - train a small YOLO model.
- `Tarining/scripts/webcam_detect.py` - run detection from a webcam.
- `Tarining/scripts/video_detect.py` - run detection on a video file.
- `Tarining/scripts/export_onnx.py` - export a model to ONNX.
- `Tarining/scripts/serial_viewer.py` - view serial camera output.

## Model Files

The repository currently includes YOLO weights such as:

- `Tarining/yolo11n.pt`
- `Tarining/yolov8s.pt`
- `Tarining/runs/yolo11n-rpi-416/weights/best.pt`
- `Tarining/runs/yolo11n-rpi-416/weights/last.pt`

These files are useful for reproducing the current experiments, but they make
the repository large. If the project grows, consider moving weights and datasets
to Releases or external storage.
