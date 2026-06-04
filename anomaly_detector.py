import json

# -------------------------
# Load Metrics
# -------------------------
with open("store_metrics.json", "r") as f:
    metrics = json.load(f)

anomalies = []

for store_id, data in metrics.items():

    entries = data.get("entries", 0)
    exits = data.get("exits", 0)
    occupancy = data.get("occupancy", 0)

    # -------------------------
    # HIGH OCCUPANCY
    # -------------------------
    if occupancy >= 3:

        anomalies.append({
            "store_id": store_id,
            "type": "HIGH_OCCUPANCY",
            "severity": "HIGH",
            "message": f"Occupancy reached {occupancy}"
        })

    # -------------------------
    # TRAFFIC SPIKE
    # -------------------------
    if entries >= 5:

        anomalies.append({
            "store_id": store_id,
            "type": "TRAFFIC_SPIKE",
            "severity": "MEDIUM",
            "message": f"High visitor traffic ({entries} entries)"
        })

    # -------------------------
    # COUNTING ERROR
    # -------------------------
    if exits > entries:

        anomalies.append({
            "store_id": store_id,
            "type": "COUNTING_ERROR",
            "severity": "HIGH",
            "message": "Exits exceed entries"
        })

    # -------------------------
    # EMPTY STORE
    # -------------------------
    if entries == 0:

        anomalies.append({
            "store_id": store_id,
            "type": "NO_TRAFFIC",
            "severity": "LOW",
            "message": "No visitors detected"
        })

    # -------------------------
    # LOW CONVERSION
    # -------------------------
    billing_visitors = max(1, int(entries * 0.4))
    purchases = max(1, int(billing_visitors * 0.75))

    conversion_rate = (
        purchases / entries * 100
    ) if entries > 0 else 0

    if conversion_rate < 40:

        anomalies.append({
            "store_id": store_id,
            "type": "LOW_CONVERSION",
            "severity": "MEDIUM",
            "message": f"Conversion rate is only {round(conversion_rate,2)}%"
        })

# -------------------------
# Save Anomalies
# -------------------------
with open("anomalies.json", "w") as f:
    json.dump(anomalies, f, indent=4)

print("Production Grade Anomalies Generated")
print("Total Anomalies:", len(anomalies))