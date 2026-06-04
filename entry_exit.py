from ultralytics import YOLO

model = YOLO("yolov8n.pt")

ENTRY_LINE_X = 850

results = model.track(
    source="videos/CAM 3 - entry.mp4",
    tracker="bytetrack.yaml",
    persist=True,
    save=True,
    classes=[0],
    conf=0.4,
    imgsz=256,
    vid_stride=5
)

print("Entry Exit Analysis Complete")