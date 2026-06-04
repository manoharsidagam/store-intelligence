# 🏪 Multi-Store Intelligence Platform

## Problem Statement

Retail stores generate large amounts of customer activity every day, but store managers often lack real-time visibility into visitor traffic, occupancy levels, customer journeys, conversion performance, and operational issues.

Without actionable insights, it becomes difficult to optimize store operations and improve customer experience.

---

## Solution

This project delivers an AI-powered Store Intelligence Platform that transforms raw store events into meaningful business insights.

Using computer vision, event processing, anomaly detection, and real-time analytics, the system enables managers to monitor store performance, understand customer behavior, and identify operational issues instantly.

---

## Core Capabilities

* Real-time Entry & Exit Tracking
* Occupancy Monitoring
* Customer Journey Analytics
* Conversion Funnel Tracking
* Purchase Correlation
* Anomaly Detection Engine
* Multi-Store Performance Monitoring
* Executive Decision Dashboard
* Dockerized Deployment

---

## System Architecture

Customer Events

↓

Event Processing Engine

↓

FastAPI Analytics Layer

↓

Metrics & Funnel Engine

↓

Anomaly Detection Engine

↓

Streamlit Executive Dashboard

---

## Key Business Metrics

* Visitor Count
* Occupancy
* Billing Visitors
* Purchases
* Conversion Rate
* Health Score
* Active Anomalies

---

## Available APIs

### GET /health

Returns application health status.

### GET /events

Returns all generated store events.

### GET /metrics

Returns aggregated business metrics.

### GET /stores/{store_id}/metrics

Returns store-level performance metrics.

### GET /stores/{store_id}/funnel

Returns customer funnel statistics.

### GET /anomalies

Returns active operational anomalies.

---

## Dashboard Features

* Executive KPI Summary
* Multi-Store Monitoring
* Funnel Analytics
* Health Monitoring
* Live Event Feed
* Anomaly Alerts
* Auto Refresh Dashboard

---

## Local Setup

Install Dependencies:

pip install -r requirements.txt

Start Backend:

uvicorn api:app --reload

Launch Dashboard:

streamlit run dashboard_ui.py

---

## Docker Deployment

Build:

docker build -t store-intelligence .

Run:

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
## AI-Assisted Decisions

### 1. Detection Model Selection

During development, AI was used to compare YOLOv8, YOLOv9, and RT-DETR for retail analytics use cases.

AI suggested YOLOv8 because of its balance between inference speed, accuracy, and community support.

After experimentation, YOLOv8 combined with ByteTrack was selected because it provided reliable person tracking while remaining lightweight enough for real-time processing.

---

### 2. Event Schema Design

AI suggested including session_id, visitor_id, confidence scores, and metadata fields to improve event traceability and analytics accuracy.

The final schema was adopted with minor modifications to better support funnel analysis and anomaly detection requirements.

---

### 3. Dashboard Design

AI-assisted brainstorming was used to evaluate different dashboard layouts.

The initial suggestion focused on raw event monitoring, but it was later modified into an executive-style dashboard showing KPIs, conversion funnels, health score, and anomaly alerts.

This provided a more business-oriented view of store performance.

## Future Scope

* Real-Time Video Analytics
* Cloud Deployment
* Predictive Traffic Forecasting
* AI-Based Recommendation Engine
* Advanced Customer Behavior Analysis
* Multi-Camera Visitor Tracking
