# SIET AI Governance Rules

---

## 1. System Purpose

SIET predicts idle infrastructure capacity and optimizes allocation while preserving fairness and governance integrity.

The system provides recommendations only. Final authority remains with administrators.

---

## 2. Data Governance

### Data Used
- Room metadata
- Historical booking data
- Booking request metadata

### Data Not Used
- Personal identifiers
- Surveillance data
- Biometric inputs

All MVP data stored locally.

---

## 3. Predictive Model Constraints

- Models provide advisory predictions.
- Confidence scores must accompany predictions.
- Low-confidence predictions require manual review.
- No automatic booking confirmations.

---

## 4. Allocation Fairness Rules

Priority tiers:

1. Academic / Institutional
2. Public Service / NGO
3. Commercial / External

Additional constraints:
- Capacity enforcement
- No time conflicts
- Stakeholder usage cap
- Transparent scoring logic

---

## 5. Simulation Integrity

- Simulations must not alter live data.
- Simulated results clearly labeled.
- Deterministic output given identical inputs.

---

## 6. Bias Mitigation

- Tier-based priority weighting
- Usage share tracking
- Allocation fairness score logging

---

## 7. Transparency

For each allocation decision log:
- Idle probability
- Demand intensity
- Priority tier applied
- Optimization objective value

---

## 8. Logging & Audit Trail

All actions log:
- Timestamp
- Input parameters
- Optimization result
- Override reason (if applicable)

Logs are immutable.

---

## 9. Fallback Policy

If model confidence < threshold:
- Flag for manual review.

If optimization fails:
- Revert to first-come-first-serve heuristic.

---

## 10. Governance Override

Administrators may:
- Override allocation
- Lock rooms
- Adjust tier weights

All overrides must be logged.