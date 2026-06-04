# 🏪 Multi-Store Intelligence Dashboard

## Overview

Retail stores need real-time visibility into customer traffic, occupancy, conversion rates, and operational issues.

This project provides an AI-powered Store Intelligence System that tracks customer movement, generates business events, detects anomalies, and visualizes key metrics through an interactive dashboard.

The platform helps store managers make faster and smarter operational decisions.

---

## Key Features

✅ Entry / Exit Tracking

✅ Occupancy Monitoring

✅ Customer Journey Tracking

✅ Conversion Funnel Analytics

✅ Purchase Monitoring

✅ Real-Time Anomaly Detection

✅ Executive KPI Dashboard

✅ Health Monitoring API

✅ Dockerized Deployment

---

## System Architecture

YOLOv8 + ByteTrack

↓

Event Generation Engine

↓

FastAPI Backend

↓

Metrics & Anomaly Engine

↓

Streamlit Dashboard

---

## Available APIs

### GET /health

Returns application health status.

### GET /events

Returns all generated store events.

### GET /metrics

Returns overall store metrics.

### GET /stores/{store_id}/metrics

Returns store-specific performance metrics.

### GET /stores/{store_id}/funnel

Returns conversion funnel statistics.

### GET /anomalies

Returns detected operational anomalies.

---

## Dashboard Highlights

* Executive KPI Summary
* Store Performance Overview
* Conversion Funnel Analysis
* Health Score Monitoring
* Active Anomaly Tracking
* Live Event Feed
* Auto Refresh Support

---

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start API:

uvicorn api:app --reload

Launch Dashboard:

streamlit run dashboard_ui.py

---

## Run Detection Pipeline

python detect.py

Generated events are stored in events.json

## Start API

uvicorn api:app --reload

## Start Dashboard

streamlit run dashboard_ui.py

## Docker

Build Image:

docker build -t store-intelligence .

Run Container:

docker run -p 8000:8000 store-intelligence

---

## Technology Stack

* Python
* FastAPI
* Streamlit
* Pandas
* YOLOv8
* ByteTrack
* Docker

---

## Future Improvements

* Real-Time Video Processing
* Database Integration
* Predictive Analytics
* Advanced AI-Based Anomaly Detection
* Multi-Camera Tracking
* Cloud Deployment Support

## Test Coverage

The project includes tests for:

- Health Endpoint
- Events Endpoint
- Anomaly Endpoint
- Store Metrics Endpoint
- Entry Events
- Exit Events
- Purchase Events
- Session Deduplication
- Empty Event Handling

Run Tests:6 passed


## Dashboard Preview

### Executive KPI Dashboard
![Dashboard](screenshots/dashboard.png.png)

### Conversion Funnel

![Funnel](screenshots/funnels.png.png)


### Active Anomalies

![Anomalies](screenshots/anomalies.png.png)

### Docker Deployment

![Docker](screenshots/docker.png.png)

### API Documentation

![Swagger](screenshots/swagger.png.png)


