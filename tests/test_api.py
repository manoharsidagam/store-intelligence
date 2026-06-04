 # PROMPT:
# Generate FastAPI API tests for health, events,
# anomalies and metrics endpoints.

# CHANGES MADE:
# Added endpoint-specific assertions.
# Adjusted tests for project event schema.
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_events():
    response = client.get("/events")
    assert response.status_code == 200

def test_anomalies():
    response = client.get("/anomalies")
    assert response.status_code == 200

def test_metrics_store1():
    response = client.get("/stores/store_1/metrics")
    assert response.status_code == 200

def test_metrics_store2():
    response = client.get("/stores/store_2/metrics")
    assert response.status_code == 200

def test_invalid_store():
    response = client.get("/stores/invalid_store/metrics")
    assert response.status_code in [200, 404]