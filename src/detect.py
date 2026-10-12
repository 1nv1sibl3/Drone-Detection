import argparse
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "models" / "best.pt"

def main():
    parser = argparse.ArgumentParser(description="Drone detection")
    parser.add_argument("--source", required=True,
                        help="Image, video, directory, or webcam index")
    parser.add_argument("--model", default=str(DEFAULT_MODEL))
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--imgsz", type=int, default=960)
    parser.add_argument("--device", default=None,
                        help="Examples: 0 for GPU, cpu for CPU")
    parser.add_argument("--project", default="runs/detect")
    parser.add_argument("--name", default="predict")
    args = parser.parse_args()

    model = YOLO(args.model)
    kwargs = {
        "source": int(args.source) if args.source.isdigit()
                  else args.source,
        "conf": args.conf,
        "imgsz": args.imgsz,
        "project": args.project,
        "name": args.name,
        "save": True,
    }
    if args.device is not None:
        kwargs["device"] = args.device

    results = model.predict(**kwargs)
    print(f"Processed {len(results)} result(s).")
    print(f"Annotated output: {args.project}/{args.name}")

if __name__ == "__main__":
    main()
