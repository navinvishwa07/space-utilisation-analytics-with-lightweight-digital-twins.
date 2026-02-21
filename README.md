# Shared Infrastructure Exchange Twin (SIET)

Predictive Space-Utilisation Analytics with Fairness-Aware Optimization.

---

## Overview

Shared Infrastructure Exchange Twin (SIET) is a lightweight digital twin platform that predicts idle infrastructure capacity and intelligently redistributes underutilised spaces using optimization and governance-aware allocation logic.

Unlike traditional occupancy dashboards, SIET predicts unused capacity before waste occurs and allocates it fairly across stakeholders using constraint optimization and simulation.

This repository contains the hackathon MVP implementation.

---

## Hackathon Topic Interpretation

**Space-Utilisation Analytics with Lightweight Digital Twins**

- **Space-utilisation analytics** analyzes patterns of room usage to identify idle capacity and forecast demand.
- A **lightweight digital twin** is a data-driven virtual model of real infrastructure that can predict behaviour without expensive hardware.
- SIET combines predictive modelling with fairness-aware allocation and simulation to go beyond passive dashboards.

---

## Problem Statement

Institutions suffer from underutilised infrastructure because existing systems lack:

- Predictive visibility into future availability
- Methods to intelligently redistribute idle space
- Fair and transparent allocation policies
- What-if simulation tools to evaluate impact

SIET answers:  
**“How can we unlock idle infrastructure capacity safely, efficiently, and predictively?”**

---

## 🎯 MVP Features

- Digital twin model for 10–15 rooms
- Idle probability prediction (Scikit-learn)
- Demand intensity forecasting
- Fairness-aware allocation engine (OR-Tools)
- What-if simulation engine
- Allocation audit logging
- Streamlit dashboard interface

---

## System Overview

Users  
→ Streamlit Dashboard  
→ FastAPI Backend  
→ Prediction Module  
→ Allocation Engine  
→ SQLite Database  

See `/docs/ARCHITECTURE.md` for full technical architecture.

---

## AI Governance Principles

SIET follows clear governance:
- Advisory predictions only
- Confidence-scores enforced
- Tier-based fairness logic
- Stakeholder usage caps
- Deterministic simulation outcomes
- Full audit trail
- Human override required

See `/docs/AI_Rules.md` for detailed policy.

---

## 🛠️ Technology Stack

**Backend:** Python, FastAPI, SQLite  
**AI & Optimization:** Pandas, NumPy, Scikit-learn, OR-Tools  
**Frontend:** Streamlit  
**DevOps:** Docker-ready architecture

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/navinvishwa07/AMDSlighshot-space-utilisation-analytics-with-lightweight-digital-twins.git
cd AMDSlighshot-space-utilisation-with-lightweight-digital-twins
