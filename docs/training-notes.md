# Training Notes

## Dataset

Source: Kaggle Drone YOLO Detection dataset.

The prepared dataset used YOLO-format labels and one class:
`0: drone`.

The prepared split used a random 80/20 train/validation split
with seed 42. Images with empty label files were excluded from
this first run because at least one inspected empty-label sample
contained a visible drone. Two images without labels were also
excluded.

## Training configuration

```python
from ultralytics import YOLO

model = YOLO("yolo26m.pt")
model.train(
    data="/content/drone_yolo/data.yaml",
    epochs=10,
    imgsz=960,
    batch=8,
    patience=10,
    device=0,
    workers=2,
    project="/content/runs",
    name="drone_detection_10ep",
    seed=42,
)
```

## Recorded best-checkpoint metrics

- Precision: 0.946
- Recall: 0.916
- mAP@50: 0.965
- mAP@50-95: 0.516

The checkpoint copied into this repository is `best.pt`.

## Caveats and future work

The random split can put visually similar frames in both sets,
which may inflate validation metrics. A future evaluation should
split by video or capture session. Add verified negative/background
images and evaluate night footage and shadows before relying on
the model in deployment.
