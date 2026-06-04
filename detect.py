from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="videos/CAM 2 - zone.mp4",
    tracker="bytetrack.yaml",
    persist=True,
    save=True,
    classes=[0],
    conf=0.4,
    imgsz=320,
    vid_stride=3
)

print("Tracking Complete")