# SIET Hackathon Plan

---

## Phase 1: Data Modeling

- Define room schema
- Generate synthetic booking history
- Implement SQLite storage

Deliverable: Functional digital twin dataset

---

## Phase 2: Availability Model

- Feature engineering
- Train logistic regression or random forest
- Output idle probability

Deliverable: Working predictor API

---

## Phase 3: Demand Forecast

- Aggregate booking requests
- Implement time-based forecasting

Deliverable: Demand intensity score

---

## Phase 4: Allocation Engine

- Implement OR-Tools solver
- Add fairness constraints
- Integrate predictions

Deliverable: Optimized allocation output

---

## Phase 5: What-If Simulation

- Constraint toggling
- Re-optimization
- Utilization comparison

Deliverable: Simulation mode

---

## Phase 6: Dashboard Integration

- Idle heatmap
- Allocation results table
- Simulation comparison view

Deliverable: Demo-ready interface

---

## Risks & Mitigation

Risk: Model underperformance  
Mitigation: Emphasize explainability.

Risk: Optimization complexity  
Mitigation: Limit to 10–20 rooms.

Risk: Time constraint  
Mitigation: Prioritize prediction + allocation.