from ultralytics import YOLO
import cv2
import json

model = YOLO("yolov8n.pt")

ENTRY_LINE_X = 700
BUFFER = 30

cap = cv2.VideoCapture("videos/CAM 3 - entry.mp4")

entry_count = 0
exit_count = 0

previous_positions = {}

# Prevent duplicate counting
counted_entry_ids = set()
counted_exit_ids = set()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=[0],
        conf=0.4
    )

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)

            if track_id in previous_positions:

                prev_x = previous_positions[track_id]

                # ENTRY
                if (
                    prev_x > ENTRY_LINE_X + BUFFER
                    and center_x < ENTRY_LINE_X - BUFFER
                    and track_id not in counted_entry_ids
                ):

                    entry_count += 1
                    counted_entry_ids.add(track_id)

                    print(f"ENTRY : {int(track_id)}")

                # EXIT
                elif (
                    prev_x < ENTRY_LINE_X - BUFFER
                    and center_x > ENTRY_LINE_X + BUFFER
                    and track_id not in counted_exit_ids
                ):

                    exit_count += 1
                    counted_exit_ids.add(track_id)

                    print(f"EXIT : {int(track_id)}")

            previous_positions[track_id] = center_x

cap.release()

print("Entries =", entry_count)
print("Exits =", exit_count)
print("Occupancy =", entry_count - exit_count)

# -------------------------
# Update only Store 1 data
# -------------------------

try:
    with open("store_metrics.json", "r") as f:
        metrics = json.load(f)
except:
    metrics = {}

metrics["store_1"] = {
    "entries": entry_count,
    "exits": exit_count,
    "occupancy": entry_count - exit_count
}

with open("store_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Store 1 metrics saved")