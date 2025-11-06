import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Run YOLO predictions on dataset images and save annotated outputs.")
	project_root = Path(__file__).resolve().parent.parent
	default_weights = project_root / "runs" / "yolo11n-rpi-416" / "weights" / "best.pt"
	# Predict over yolo-data images by default (supports flat layout)
	default_source_images = project_root / "yolo-data" / "images"
	default_outdir = project_root / "predictions"

	parser.add_argument("--weights", type=str, default=str(default_weights), help="Path to model weights .pt")
	parser.add_argument("--sources", type=str, nargs="*", default=[str(default_source_images)], help="Image folder(s) or file(s) to run inference on")
	parser.add_argument("--outdir", type=str, default=str(default_outdir), help="Root directory to save annotated results")
	parser.add_argument("--imgsz", type=int, default=640, help="Inference image size")
	parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
	parser.add_argument("--device", type=str, default="cpu", help="Device to use: 'cpu' or CUDA index like '0'")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	model = YOLO(args.weights)
	project_dir = Path(args.outdir)
	project_dir.mkdir(parents=True, exist_ok=True)

	for source in args.sources:
		source_path = Path(source)
		name = source_path.name if source_path.exists() else Path(source).name
		model.predict(
			source=str(source),
			save=True,          # save images with boxes drawn
			save_txt=True,      # save txt labels
			save_conf=True,     # save confidence in txt
			exist_ok=True,      # do not error if folder exists
			line_width=2,       # box thickness
			show_labels=True,
			show_conf=True,
			imgsz=args.imgsz,
			conf=args.conf,
			device=args.device,
			project=str(project_dir),
			name=name,
		)

	print(f"Predictions saved under: {project_dir}")


if __name__ == "__main__":
	main()


