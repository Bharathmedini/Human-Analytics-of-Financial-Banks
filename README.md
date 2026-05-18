# 📊 HDFC Bank — Financial Market Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?style=flat-square&logo=postgresql)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi)
![NSE](https://img.shields.io/badge/Exchange-NSE%20India-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> **End-to-end equity analytics pipeline for HDFC Bank (NSE: HDFCBANK)**  
> Covering 245 trading days | Jul 2019 – Jun 2020 | COVID-19 Market Volatility Study

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Key Highlights](#key-highlights)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Dashboard Layers](#dashboard-layers)
- [Key Performance Metrics](#key-performance-metrics)
- [Quarterly Scorecard](#quarterly-scorecard)
- [Extreme Events Detected](#extreme-events-detected)
- [Hardware Requirements](#hardware-requirements)
- [Challenges & Solutions](#challenges--solutions)
- [Future Scope](#future-scope)
- [Author](#author)

---

## 📖 About the Project

This project delivers a comprehensive **Financial Market Analytics Dashboard** for **HDFC Bank**, India's largest private sector bank by market capitalisation (NSE: HDFCBANK).

The fiscal period **July 2019 – June 2020** was selected deliberately — it captures:
- The **September 2019 stock split** causing a mechanical −49.67% single-day price drop
- The **COVID-19 pandemic crash** of March 2020, driving the stock to a trough of ₹767.7
- A dramatic **recovery rally** with a best single-day return of +11.60% on 25 Mar 2020

The pipeline processes **245 trading days** of NSE EQ series data across **21 columns** (15 raw + 6 derived), cleaned via Python (pandas) and reconciled through **25 SQL queries**, achieving:

```
✅  Zero missing values
✅  Zero duplicate records
✅  Full audit log via SQL
```

---

## ⚡ Key Highlights

| Feature | Detail |
|--------|--------|
| 📅 Period | Jul 2019 – Jun 2020 (FY) |
| 📈 Trading Days | 245 |
| 🗂️ Data Columns | 21 (15 raw + 6 derived) |
| 🔍 SQL Queries | 25 reconciliation queries |
| ❌ Missing Values | 0 |
| ❌ Duplicates | 0 |
| 🧱 Architecture | Diagnostic + Prescriptive Layers |

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| **Python 3.10 + pandas** | Data cleaning, feature engineering, pipeline |
| **SQL (PostgreSQL)** | 25-query reconciliation & audit log |
| **Power BI Desktop** | Dashboard visualisation & publishing |
| **NSE Data API** | Raw equity data extraction (EQ series) |
| **Jupyter Notebook** | Exploratory analysis & documentation |

---

## 🏗️ System Architecture — Data Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA PIPELINE FLOW                          │
├──────────────┬──────────────┬──────────────┬───────────────────┤
│ 01 EXTRACT   │ 02 CLEAN     │ 03 RECONCILE │ 04 ANALYSE        │
│ (20%)        │ (25%)        │ (25%)        │ (30%)             │
│              │              │              │                   │
│ NSE Data API │ 7 Python     │ 6 cross-     │ 8 final queries   │
│ 5 SQL Queries│ checks       │ checks       │ 4-level model     │
│ HRIS Pull    │ pandas       │ SQL audit    │ Diag + Prescriptive│
│              │ pipeline     │ log          │                   │
│              │ 0 nulls      │ Schema       │                   │
│              │ 0 dupes      │ validation   │                   │
└──────────────┴──────────────┴──────────────┴───────────────────┘
         OUTPUT: 245 rows · 21 columns · Power BI Dashboard
```

---

## 📊 Dashboard Layers

### 🔵 Diagnostic Layer
Identifies *what happened* and *why*:
- Pre-COVID vs COVID-onset market segmentation
- Extreme event detection & classification
- Monthly close price with 30-day moving average overlay
- Daily return distribution analysis

### 🟢 Prescriptive Layer
Translates data into *actionable insights*:
- Quarterly scorecard generation
- Delivery ratio as conviction signal (long-term holders vs intraday traders)
- Trend-based intervention triggers
- Business recommendations per quarter

---

## 📈 Key Performance Metrics

| Metric | Value | Context |
|--------|-------|---------|
| 🔺 Peak Price | ₹2,495 | July 2019 |
| 🔻 Trough Price | ₹767.7 | March 2020 (COVID crash) |
| 📊 Avg Close (FY) | ₹1,381 | Full-year average |
| 📉 Worst Day Return | −49.67% | 19 Sep 2019 *(stock split — mechanical)* |
| 📈 Best Day Return | +11.60% | 25 Mar 2020 *(relief rally)* |
| 🚚 Avg Delivery Ratio | 54.2% | Conviction ratio |
| 💰 Total Turnover | ₹2.64 Trillion | Full year |
| 📐 Daily Volatility (σ) | 4.05% | Std dev of daily returns |

> ⚠️ **Note:** The −49.67% on 19 Sep 2019 is a **mechanical price adjustment** due to a stock split — not an actual market loss. All visual representations include an annotation to prevent misinterpretation.

---

## 🗓️ Quarterly Scorecard

| Quarter | Days | Avg Close | Volume | Delivery | Return | Status |
|---------|------|-----------|--------|----------|--------|--------|
| **2019 Q3** | 62 | ₹2,150 | 299M | 58.75% | −48.9% | ⚠️ Weak |
| **2019 Q4** | 61 | ₹1,252 | 367M | 59.59% | +3.9% | 🟡 Stable |
| **2020 Q1** | 64 | ₹1,156 | 742M | 61.08% | −35.2% | 🔴 Crisis |
| **2020 Q2** | 58 | ₹943 | 1.23B | 38.82% | +25.0% | 🟢 Rebound |

**Prescriptive Insights:**
- **Q3 2019** — Intervention needed; monitor split impact and stabilise investor confidence
- **Q4 2019** — Recovery trend; monitor delivery ratio for long-term conviction signals
- **Q1 2020** — COVID crash; review risk controls; high delivery ratio shows institutional holding
- **Q2 2020** — Low delivery (38.82%) reflects short-term day trading surge during recovery bounce

---

## 🚨 Extreme Events Detected

| Date | Event Type | Close ₹ | Return % | Volume (M) |
|------|-----------|---------|----------|------------|
| 19 Sep 2019 | Stock Split *(Mechanical)* | ₹1,101 | −49.67% | 5.3 |
| 23 Mar 2020 | COVID Crash *(Peak)* | ₹771 | −12.61% | 25.1 |
| 18 Mar 2020 | COVID Crash | ₹877 | −10.07% | 30.6 |
| 25 Mar 2020 | Relief Rally | ₹857 | +11.60% | 23.6 |
| 07 Apr 2020 | Recovery Rally | ₹896 | +10.11% | 30.2 |
| 12 Mar 2020 | COVID Panic | ₹1,021 | −8.30% | 29.5 |
| 20 Sep 2019 | Tax Cut Rally | ₹1,200 | +8.95% | 23.1 |

---

## 💻 Hardware Requirements

| Component | Specification |
|-----------|--------------|
| Processor | Intel Core i5 / AMD Ryzen 5 or higher |
| RAM | 8 GB minimum (16 GB recommended) |
| Storage | SSD 256 GB+ (for fast SQL queries) |
| OS | Windows 10/11 or Ubuntu 20.04+ |
| Display | 1920×1080 for dashboard rendering |

> 💡 All data processing is performed on cloud-compatible infrastructure. The pipeline is **containerisable via Docker** for team deployment.

---

## 🧩 Challenges & Solutions

| # | Challenge | Solution |
|---|-----------|---------|
| 1 | Mislabelled dashboard (HR vs Financial) | Rebranded all headers from "HR Analytics / HRIS" to "Financial Market Analytics / NSE Data Pull" |
| 2 | Avg Close decimal error (1.381 vs ₹1,381) | Recalculated KPI card; verified against price range ₹767–₹2,495 |
| 3 | Typos in quarterly scorecards | Corrected "Renan" → "Return", "Reel rally" → "Relief rally" |
| 4 | Low Q2 2020 delivery (38.82%) unexplained | Added commentary on intraday trader surge during volatile recovery |
| 5 | COVID crash vs stock split confusion | Added annotation flags to distinguish Sep 2019 mechanical split from Mar 2020 crash |

---

## 🚀 Future Scope

- [ ] Integrate **live NSE data feed** for real-time monitoring
- [ ] Add **ML-based anomaly detection** for automatic market event flagging
- [ ] Extend to **multi-stock portfolio comparison** across NIFTY 50 constituents
- [ ] Build **alerting system** for extreme return thresholds
- [ ] Deploy dashboard as a **web app** using Streamlit or Flask

---

## 👤 Author

**Student Project** — May 2026  
HDFC Bank Financial Market Analytics | NSE EQ Series | Jul 2019 – Jun 2020

---

*This project is for educational and analytical purposes only. All data sourced from NSE public records.*
