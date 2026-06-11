# 🏦 Human Resource Financial Analytics of Banks
**HDFC Bank | NSE: HDFCBANK | FY Jul 2019 – Jun 2020 | 245 Trading Days**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?style=flat-square&logo=postgresql)
![PowerBI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## 🎯 The Problem

Banks generate massive HR and financial data — but leadership couldn't act on it because:

| Problem | Impact |
|---|---|
| Data sat in disconnected silos (HRIS + NSE feeds) | No unified view for decisions |
| Dashboards treated all trading days equally | COVID crash looked the same as a stock split |
| Volume data had no depth | Couldn't tell institutional holders from day traders |
| Reports arrived after events happened | Reactive, not prescriptive |
| Raw data had labelling errors & decimal mistakes | KPIs were wrong before analysis even started |

---

## 🧠 How We Solved It

**4-stage pipeline — Extract → Clean → Reconcile → Analyse**

- **Python (pandas):** 7 systematic checks → `0 nulls`, `0 duplicates`, 21 clean columns
- **25 SQL queries:** Every KPI independently verified — audit-ready for a regulated bank
- **Power BI:** Two-layer dashboard — *Diagnostic* (what happened) + *Prescriptive* (what to do)

---

## ⚡ Project Highlights

**① Separating Mechanical Events from Real Crashes**
The −49.67% drop on 19 Sep 2019 was a *stock split* — not a market loss. Most dashboards would flag it as a crisis. We annotated it as a corporate action. That distinction protects investor communications.

**② Delivery Ratio as a Conviction Signal**
Decomposed raw volume into delivery ratio (long-term holders vs. intraday traders). During the COVID crash Q1 2020, delivery hit **61.08%** — revealing institutional confidence hidden inside noisy volume data.

**③ Dual-Layer Dashboard**
Diagnostic layer for analysts. Prescriptive layer for executives. Two audiences, one clean dashboard — instead of one cluttered report that serves neither.

**④ 25-Query SQL Audit**
Every metric on the dashboard has a SQL query that independently verifies it — making the analysis defensible in a regulated banking environment.

---

## 📈 Key Numbers

| Metric | Value |
|---|---|
| Peak Price | ₹2,495 (Jul 2019) |
| Trough Price | ₹767.7 (Mar 2020 — COVID) |
| Best Single Day | +11.60% on 25 Mar 2020 |
| Worst Single Day | −49.67% on 19 Sep 2019 *(stock split)* |
| Avg Delivery Ratio | 54.2% |
| Total Turnover | ₹2.64 Trillion |
| Daily Volatility (σ) | 4.05% |

---

## 🗓️ Quarterly Scorecard

| Quarter | Return | Delivery | Status | Action |
|---|---|---|---|---|
| Q3 2019 | −48.9% | 58.75% | ⚠️ Weak | Monitor split impact |
| Q4 2019 | +3.9% | 59.59% | 🟡 Stable | Watch conviction signals |
| Q1 2020 | −35.2% | 61.08% | 🔴 Crisis | Institutions held — don't panic |
| Q2 2020 | +25.0% | 38.82% | 🟢 Rebound | Day-trader bounce — monitor sustainability |

---

## 🚀 Future Scope

- Live NSE data feed for real-time monitoring
- ML-based anomaly detection for automatic event flagging
- Extend to multi-stock NIFTY 50 comparison
- Deploy as a Streamlit web app

---

**Bharath Medini** · [LinkedIn](https://linkedin.com/in/bharath-medini) · [GitHub](https://github.com/Bharathmedini)  
*Data for educational purposes only. Source: NSE public records.*
