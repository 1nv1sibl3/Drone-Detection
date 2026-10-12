# Drone Detection using YOLO26m

A single-class drone object detector trained using the
Drone YOLO Detection dataset from Kaggle. Task given in 
Drone Club MITAOE for learning purpose/

## Model

- Architecture: YOLO26m
- Training epochs: 10
- Image size: 960
- Batch size: 8
- Seed: 42
- Class: `drone`

### Recorded validation metrics

| Metric | Result |
|---|---:|
| Precision | 94.6% |
| Recall | 91.6% |
| mAP@50 | 96.5% |
| mAP@50-95 | 51.6% |

These metrics are from the recorded validation run. The random
image split may contain similar frames across training and
validation, so results on independent footage may differ.

## Repository structure

```text
Drone-Detection/
├── models/
│   └── best.pt
├── src/
│   └── detect.py
├── docs/
│   └── training-notes.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/1nv1sibl3/Drone-Detection.git
cd Drone-Detection
pip install -r requirements.txt
```

## Run detection

For an image:

```bash
python src/detect.py --source path/to/image.jpg
```

For a video:

```bash
python src/detect.py --source path/to/video.mp4
```

For a webcam:

```bash
python src/detect.py --source 0
```

Choose a confidence threshold:

```bash
python src/detect.py --source path/to/video.mp4 --conf 0.5
```

Annotated results are saved in `runs/detect/`.

## Known limitations

- Shadows and difficult night-time footage can produce false positives.
- Validation performance does not guarantee performance in all environments.
- The first training run excluded images with empty label files;
  verified background-only images should be added in future training.

## Dataset

Dataset source:
https://www.kaggle.com/datasets/sshikamaru/drone-yolo-detection

Please check the dataset's current licence and terms before
redistributing the dataset or its contents. The dataset itself
is not included in this repository.

## Training

See [training notes](docs/training-notes.md).

## Model weights

The trained checkpoint is included at `models/best.pt`.
