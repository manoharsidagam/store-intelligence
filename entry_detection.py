from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="videos/CAM 3 - entry.mp4",
    classes=[0],
    save=True,
    conf=0.4,
    imgsz=256,
    vid_stride=5
)

print("Entry Detection Complete")