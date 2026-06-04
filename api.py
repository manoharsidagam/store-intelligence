from fastapi import FastAPI, HTTPException
from datetime import datetime
import json
import logging
from typing import Any, Dict

app = FastAPI(
    title="Store Intelligence API",
    version="2.0"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ----------------------------
# Utility Functions
# ----------------------------
def _load_json(path: str, default: Any):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return default


def load_metrics() -> Dict:
    return _load_json("store_metrics.json", {})


# ----------------------------
# Home
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "Store Intelligence API Running",
        "version": "2.0"
    }


# ----------------------------
# Health Check
# ----------------------------
@app.get("/health")
def health():

    metrics = load_metrics()
    events = _load_json("events.json", [])

    return {
        "status": "healthy",
        "service": "Store Intelligence API",
        "version": "2.0",
        "timestamp": datetime.now().isoformat(),
        "stores_loaded": len(metrics),
        "events_loaded": len(events),
        "api_status": "UP"
    }


# ----------------------------
# Events
# ----------------------------
@app.get("/events")
def events():
    logger.info("Events endpoint called")

    return _load_json("events.json", [])


# ----------------------------
# Overall Metrics
# ----------------------------
@app.get("/metrics")
def metrics():

    data = _load_json("events.json", [])

    entries = len([
        e for e in data
        if e.get("event_type") == "ENTRY"
    ])

    exits = len([
        e for e in data
        if e.get("event_type") == "EXIT"
    ])

    occupancy = entries - exits

    return {
        "entries": entries,
        "exits": exits,
        "occupancy": occupancy
    }


# ----------------------------
# Store Metrics
# ----------------------------
@app.get("/stores/{store_id}/metrics")
def store_metrics(store_id: str):

    logger.info(
        f"Metrics requested for {store_id}"
    )

    metrics = load_metrics()

    if store_id not in metrics:
        raise HTTPException(
            status_code=404,
            detail="Store not found"
        )

    events = _load_json("events.json", [])

    entries = metrics[store_id].get("entries", 0)
    exits = metrics[store_id].get("exits", 0)
    occupancy = metrics[store_id].get("occupancy", 0)

    billing_visitors = len([
        e for e in events
        if e.get("store_id") == store_id
        and e.get("event_type") == "QUEUE_COMPLETED"
    ])

    purchases = len([
        e for e in events
        if e.get("store_id") == store_id
        and e.get("event_type") == "PURCHASE"
    ])

    conversion_rate = round(
        (purchases / entries) * 100,
        2
    ) if entries > 0 else 0

    return {
        "store_id": store_id,
        "entries": entries,
        "exits": exits,
        "occupancy": occupancy,
        "billing_visitors": billing_visitors,
        "purchases": purchases,
        "conversion_rate": conversion_rate
    }


# ----------------------------
# Funnel API
# ----------------------------
@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):

    events = _load_json("events.json", [])
    metrics = load_metrics()

    if store_id not in metrics:
        raise HTTPException(
            status_code=404,
            detail="Store not found"
        )

    entry_sessions = set()
    billing_sessions = set()
    purchase_sessions = {
        e["session_id"]
        for e in events
        if e.get("store_id") == store_id
        and e.get("event_type") == "PURCHASE"
    }

    for event in events:

        if event.get("store_id") != store_id:
            continue

        session = event.get("session_id")

        if event.get("event_type") == "ENTRY":
            entry_sessions.add(session)

        elif event.get("event_type") == "QUEUE_COMPLETED":
            billing_sessions.add(session)

    entries = len(entry_sessions)
    billing = len(billing_sessions)
    purchases = len(purchase_sessions)

    billing_dropoff = round(
        ((entries - billing) / entries) * 100,
        2
    ) if entries > 0 else 0

    conversion_rate = round(
        (purchases / entries) * 100,
        2
    ) if entries > 0 else 0

    return {
        "store_id": store_id,
        "entries": entries,
        "billing_visitors": billing,
        "purchases": purchases,
        "billing_dropoff_percent": billing_dropoff,
        "conversion_rate": conversion_rate
    }


# ----------------------------
# Anomalies
# ----------------------------
@app.get("/anomalies")
def anomalies():

    logger.info(
        "Anomalies endpoint called"
    )

    return _load_json("anomalies.json", [])


# ----------------------------
# Store Summary
# ----------------------------
@app.get("/summary")
def summary():

    metrics = load_metrics()

    total_entries = sum(
        store.get("entries", 0)
        for store in metrics.values()
    )

    total_exits = sum(
        store.get("exits", 0)
        for store in metrics.values()
    )

    total_occupancy = sum(
        store.get("occupancy", 0)
        for store in metrics.values()
    )

    return {
        "stores": len(metrics),
        "total_entries": total_entries,
        "total_exits": total_exits,
        "total_occupancy": total_occupancy
    }