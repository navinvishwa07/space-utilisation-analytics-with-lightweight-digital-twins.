# SIET System Architecture

---

## High-Level Overview

Users
  ↓
Streamlit Dashboard
  ↓
FastAPI Backend
  ↓
Prediction Module → Allocation Engine
  ↓
SQLite Database

---

## Core Modules

### 1. Data Layer

Tables:
- Rooms
- Booking History
- Requests
- Allocation Logs

---

### 2. Availability Prediction Pipeline

Historical Data
→ Feature Engineering
→ Train Model (Scikit-learn)
→ Idle Probability Output
→ Confidence Score

---

### 3. Demand Forecast Pipeline

Historical Requests
→ Time Aggregation
→ Forecast Model
→ Demand Intensity Score

---

### 4. Allocation Engine (OR-Tools)

Objective:
Maximize predicted idle utilization × priority weight

Constraints:
- No conflicts
- Capacity limits
- Tier enforcement
- Stakeholder usage cap

---

### 5. Simulation Engine

Temporary constraint injection:
- Block room
- Add event
- Modify tier weight

Re-run prediction + optimization.

Return comparison metrics:
- Utilization %
- Fairness score
- Allocation delta

---

## API Endpoints

- /predict_availability
- /forecast_demand
- /optimize_allocation
- /simulate
- /audit_logs

---

## Authentication (MVP)

- Admin token authentication
- Read-only public dashboard view

---

## Scalability Plan

Post-MVP:
- PostgreSQL migration
- Separate prediction microservice
- Docker containerization
- Multi-institution federation

---

## Resilience Twin Extension

Future plug-in module:

- Indoor heat risk model
- Ventilation load estimator
- Crowd density stress predictor
- Emergency redistribution simulation

Uses same simulation + allocation framework.