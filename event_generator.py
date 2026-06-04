import json
from datetime import datetime
import pandas as pd

# -----------------------------
# Load Metrics
# -----------------------------
with open("store_metrics.json", "r") as f:
    metrics = json.load(f)

# -----------------------------
# Load POS Data
# -----------------------------
pos_df = pd.read_csv("POS_sample_transactions.csv")

events = []
event_counter = 1

for store_id, data in metrics.items():

    entries = data["entries"]
    exits = data["exits"]

    # ===================================
    # ENTRY + ZONE EVENTS
    # ===================================
    for i in range(entries):

        session_id = f"SES_{store_id}_{i+1}"
        visitor_id = f"VIS_{i+1}"
        track_id = i + 1

        # ENTRY
        events.append({
            "event_id": f"EVT_{event_counter:04d}",
            "event_version": "1.0",
            "event_type": "ENTRY",
            "timestamp": datetime.now().isoformat(),

            "store_id": store_id,
            "camera_id": "entry_camera",

            "session_id": session_id,
            "visitor_id": visitor_id,
            "track_id": track_id,

            "direction": "IN",

            "is_staff": False,

            "group_id": None,
            "group_size": None,

            "gender_pred": "Unknown",
            "age_bucket": "Unknown",

            "confidence": 0.90,

            "source": {
                "detector": "YOLOv8",
                "tracker": "ByteTrack"
            }
        })

        event_counter += 1

        # ZONE ENTER
        events.append({
            "event_id": f"EVT_{event_counter:04d}",
            "event_version": "1.0",
            "event_type": "ZONE_ENTERED",
            "timestamp": datetime.now().isoformat(),

            "store_id": store_id,
            "camera_id": "zone_camera",

            "session_id": session_id,
            "visitor_id": visitor_id,
            "track_id": track_id,

            "zone_id": "beauty_zone",
            "zone_name": "Beauty Products",

            "is_revenue_zone": True,

            "confidence": 0.91
        })

        event_counter += 1

        # ZONE EXIT
        events.append({
            "event_id": f"EVT_{event_counter:04d}",
            "event_version": "1.0",
            "event_type": "ZONE_EXITED",
            "timestamp": datetime.now().isoformat(),

            "store_id": store_id,
            "camera_id": "zone_camera",

            "session_id": session_id,
            "visitor_id": visitor_id,
            "track_id": track_id,

            "zone_id": "beauty_zone",
            "zone_name": "Beauty Products",

            "confidence": 0.91
        })

        event_counter += 1

    # ===================================
    # BILLING / QUEUE EVENTS
    # ===================================
    billing_visitors = max(1, int(entries * 0.4))

    for i in range(billing_visitors):

        session_id = f"SES_{store_id}_{i+1}"
        visitor_id = f"VIS_{i+1}"
        track_id = i + 1

        events.append({
            "event_id": f"EVT_{event_counter:04d}",
            "event_version": "1.0",

            "event_type": "QUEUE_COMPLETED",
            "timestamp": datetime.now().isoformat(),

            "store_id": store_id,
            "camera_id": "billing_camera",

            "session_id": session_id,
            "visitor_id": visitor_id,
            "track_id": track_id,

            "zone_id": "billing_zone",

            "wait_seconds": 12,
            "queue_position": 2,

            "abandoned": False
        })

        event_counter += 1
# ===================================
# PURCHASE EVENTS FROM POS
# ===================================

purchase_visitors = min(
    billing_visitors,
    len(pos_df["order_id"].unique())
)

unique_orders = (
    pos_df
    .drop_duplicates("order_id")
    .head(purchase_visitors)
)

for i, (_, order) in enumerate(unique_orders.iterrows()):

    session_id = f"SES_{store_id}_{i+1}"
    visitor_id = f"VIS_{i+1}"
    track_id = i + 1

    purchase_amount = float(order["total_amount"])

    events.append({
        "event_id": f"EVT_{event_counter:04d}",
        "event_version": "1.0",

        "event_type": "PURCHASE",

        "timestamp": datetime.now().isoformat(),

        "store_id": store_id,
        "camera_id": "billing_camera",

        "session_id": session_id,
        "visitor_id": visitor_id,
        "track_id": track_id,

        "purchase_id": str(order["order_id"]),
        "transaction_id": str(order["order_id"]),

        "zone_id": "billing_zone",

        "purchase_value": purchase_amount,

        "confidence": 0.95,

        "source": {
            "detector": "YOLOv8",
            "tracker": "ByteTrack",
            "pos_linked": True
        }
    })

    event_counter += 1

    # ===================================
    # EXIT EVENTS
    # ===================================
    for i in range(exits):

        session_id = f"SES_{store_id}_{i+1}"
        visitor_id = f"VIS_{i+1}"
        track_id = i + 1

        events.append({
            "event_id": f"EVT_{event_counter:04d}",
            "event_version": "1.0",

            "event_type": "EXIT",

            "timestamp": datetime.now().isoformat(),

            "store_id": store_id,

            "camera_id": "entry_camera",

            "session_id": session_id,

            "visitor_id": visitor_id,

            "track_id": track_id,

            "direction": "OUT",

            "confidence": 0.90,

            "source": {
                "detector": "YOLOv8",
                "tracker": "ByteTrack"
            }
        })

        event_counter += 1

# ===================================
# SAVE EVENTS
# ===================================
with open("events.json", "w") as f:
    json.dump(events, f, indent=4)

print("Production Grade Events Generated Successfully")
print("Total Events:", len(events))