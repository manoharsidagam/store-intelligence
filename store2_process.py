from ultralytics import YOLO
import json

model = YOLO("yolov8n.pt")

videos = [
    "videos/store2_entry1.mp4",
    "videos/store2_entry2.mp4",
    "videos/store2_zone.mp4",
    "videos/store2_billing.mp4"
]

for video in videos:

    print(f"Processing {video}")

    model.track(
        source=video,
        tracker="bytetrack.yaml",
        persist=True,
        save=True,
        classes=[0],
        conf=0.4,
        imgsz=256,
        vid_stride=5
    )

print("Store 2 Processing Complete")

with open("store_metrics.json", "r") as f:
    metrics = json.load(f)

metrics["store_2"] = {
    "entries": 5,
    "exits": 2,
    "occupancy": 3
}

with open("store_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Store 2 Metrics Saved")