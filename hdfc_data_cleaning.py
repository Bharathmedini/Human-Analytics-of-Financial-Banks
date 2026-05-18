"""
=============================================================
  HDFC Bank — Financial Market Analytics
  Data Cleaning Pipeline (Python + pandas)
  NSE EQ Series | Jul 2019 – Jun 2020 | 245 Trading Days
=============================================================
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# STEP 1 — LOAD RAW DATA
# ─────────────────────────────────────────────

df = pd.read_csv("hdfc_bank_cleaned.csv")

print("=" * 60)
print("  HDFC Bank Data Cleaning Pipeline")
print("=" * 60)
print(f"\n[LOAD] Raw shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"       Columns: {list(df.columns)}\n")


# ─────────────────────────────────────────────
# STEP 2 — INSPECT DATA TYPES
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 2] Data Types Before Cleaning")
print("─" * 60)
print(df.dtypes)
print()


# ─────────────────────────────────────────────
# STEP 3 — FIX DATE COLUMN
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 3] Parsing 'date' Column to datetime")
print("─" * 60)

df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")

invalid_dates = df["date"].isna().sum()
print(f"  ✅ 'date' converted to datetime64")
print(f"  Invalid / unparseable dates: {invalid_dates}")
print(f"  Date range: {df['date'].min().date()} → {df['date'].max().date()}")
print()


# ─────────────────────────────────────────────
# STEP 4 — MISSING VALUES AUDIT
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 4] Missing Values Audit")
print("─" * 60)

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct})
missing_report = missing_report[missing_report["Missing Count"] > 0]

if missing_report.empty:
    print("  ✅ No missing values found across all 21 columns.")
else:
    print(missing_report)
    # Fill numeric columns with column median
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    # Fill categorical columns with mode
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    print("  ✅ Nulls filled — numeric→median, categorical→mode")
print()


# ─────────────────────────────────────────────
# STEP 5 — DUPLICATE ROWS CHECK
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 5] Duplicate Rows Check")
print("─" * 60)

dupes = df.duplicated().sum()
date_dupes = df.duplicated(subset=["date"]).sum()

print(f"  Full-row duplicates : {dupes}")
print(f"  Duplicate dates     : {date_dupes}")

if dupes > 0:
    df = df.drop_duplicates()
    print(f"  ✅ {dupes} duplicate(s) removed. New shape: {df.shape}")
else:
    print("  ✅ No duplicates found.")
print()


# ─────────────────────────────────────────────
# STEP 6 — STANDARDISE COLUMN NAMES
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 6] Standardise Column Names")
print("─" * 60)

# Rename special-character columns to clean snake_case
rename_map = {
    "daily_return_%": "daily_return_pct",
    "delivery_ratio_%": "delivery_ratio_pct",
    "dly_qt_to_traded_qty": "delivery_qty_ratio",
}
df.rename(columns=rename_map, inplace=True)

# Lowercase all column names and strip whitespace
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

print("  ✅ Renamed columns:")
for old, new in rename_map.items():
    print(f"     '{old}'  →  '{new}'")
print()


# ─────────────────────────────────────────────
# STEP 7 — STANDARDISE CATEGORICAL COLUMNS
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 7] Standardise Categorical Columns")
print("─" * 60)

# symbol and series should be consistent uppercase strings
df["symbol"] = df["symbol"].str.strip().str.upper()
df["series"] = df["series"].str.strip().str.upper()

print(f"  Unique symbols : {df['symbol'].unique().tolist()}")
print(f"  Unique series  : {df['series'].unique().tolist()}")
print("  ✅ symbol and series standardised to uppercase.")
print()


# ─────────────────────────────────────────────
# STEP 8 — VALIDATE NUMERIC PRICE COLUMNS
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 8] Validate Numeric Price Columns")
print("─" * 60)

price_cols = ["prev_close", "open_price", "high_price", "low_price",
              "last_price", "close_price", "average_price"]

for col in price_cols:
    neg = (df[col] < 0).sum()
    zero = (df[col] == 0).sum()
    print(f"  {col:20s}  min={df[col].min():.2f}  max={df[col].max():.2f}  "
          f"negatives={neg}  zeros={zero}")

print()

# Logical check: high_price >= low_price always
invalid_hl = (df["high_price"] < df["low_price"]).sum()
print(f"  high_price < low_price violations: {invalid_hl}")
if invalid_hl == 0:
    print("  ✅ All high/low price relationships are valid.")
print()


# ─────────────────────────────────────────────
# STEP 9 — VALIDATE VOLUME & DELIVERY COLUMNS
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 9] Validate Volume & Delivery Columns")
print("─" * 60)

vol_cols = ["total_traded_quantity", "deliverable_qty", "no_of_trades"]
for col in vol_cols:
    neg = (df[col] < 0).sum()
    print(f"  {col:30s}  min={df[col].min():,}  negatives={neg}")

# delivery_qty should never exceed total_traded_quantity
invalid_del = (df["deliverable_qty"] > df["total_traded_quantity"]).sum()
print(f"\n  deliverable_qty > total_traded_quantity violations: {invalid_del}")
if invalid_del == 0:
    print("  ✅ All delivery quantity values are within traded quantity.")
print()


# ─────────────────────────────────────────────
# STEP 10 — VALIDATE RATIO / PERCENTAGE COLUMNS
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 10] Validate Ratio / Percentage Columns")
print("─" * 60)

ratio_cols = ["delivery_qty_ratio", "delivery_ratio_pct"]
for col in ratio_cols:
    out_of_range = ((df[col] < 0) | (df[col] > 100)).sum()
    print(f"  {col:30s}  min={df[col].min():.2f}  max={df[col].max():.2f}  "
          f"out-of-range(0–100): {out_of_range}")

print("  ✅ All ratio columns within expected 0–100 range.")
print()


# ─────────────────────────────────────────────
# STEP 11 — DERIVE / VERIFY CALCULATED COLUMNS
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 11] Verify Derived Columns")
print("─" * 60)

# Re-derive daily_return_pct and compare to existing
df["daily_return_check"] = (
    (df["close_price"] - df["prev_close"]) / df["prev_close"] * 100
).round(4)

discrepancy = (df["daily_return_check"] - df["daily_return_pct"]).abs()
max_disc = discrepancy.max()
print(f"  Max discrepancy in daily_return_pct (re-derived vs stored): {max_disc:.6f}%")
if max_disc < 0.01:
    print("  ✅ daily_return_pct matches re-derived values (tolerance < 0.01%).")
df.drop(columns=["daily_return_check"], inplace=True)

# Re-derive price_range and compare
df["price_range_check"] = (df["high_price"] - df["low_price"]).round(2)
pr_disc = (df["price_range_check"] - df["price_range"]).abs().max()
print(f"  Max discrepancy in price_range (re-derived vs stored): {pr_disc:.4f}")
if pr_disc < 0.01:
    print("  ✅ price_range matches re-derived values.")
df.drop(columns=["price_range_check"], inplace=True)
print()


# ─────────────────────────────────────────────
# STEP 12 — FLAG EXTREME EVENTS (STOCK SPLIT + COVID)
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 12] Flag Extreme Events")
print("─" * 60)

RETURN_THRESHOLD = 8.0  # % magnitude

df["event_flag"] = "Normal"

# Stock split mechanical drop (19 Sep 2019)
split_mask = df["date"] == pd.Timestamp("2019-09-19")
df.loc[split_mask, "event_flag"] = "Stock Split"

# COVID crash window (Feb – Apr 2020)
covid_crash = (
    (df["date"] >= "2020-02-01") &
    (df["date"] <= "2020-04-30") &
    (df["daily_return_pct"] < -RETURN_THRESHOLD)
)
df.loc[covid_crash, "event_flag"] = "COVID Crash"

# Relief/recovery rallies
rally = (
    (df["date"] >= "2020-03-01") &
    (df["daily_return_pct"] > RETURN_THRESHOLD)
)
df.loc[rally, "event_flag"] = "Relief Rally"

event_summary = df["event_flag"].value_counts()
print(event_summary.to_string())
print("  ✅ event_flag column added.")
print()


# ─────────────────────────────────────────────
# STEP 13 — SORT & RESET INDEX
# ─────────────────────────────────────────────

print("─" * 60)
print("[STEP 13] Sort by Date & Reset Index")
print("─" * 60)

df = df.sort_values("date").reset_index(drop=True)
print(f"  ✅ Sorted chronologically. Index reset (0 → {len(df)-1}).")
print()


# ─────────────────────────────────────────────
# STEP 14 — FINAL AUDIT SUMMARY
# ─────────────────────────────────────────────

print("=" * 60)
print("  FINAL AUDIT SUMMARY")
print("=" * 60)
print(f"  Rows             : {df.shape[0]}")
print(f"  Columns          : {df.shape[1]}")
print(f"  Missing Values   : {df.isnull().sum().sum()}")
print(f"  Duplicate Rows   : {df.duplicated().sum()}")
print(f"  Date Range       : {df['date'].min().date()} → {df['date'].max().date()}")
print(f"  Trading Days     : {df['date'].nunique()}")
print(f"  Symbol           : {df['symbol'].unique().tolist()}")
print(f"  Price Range (₹)  : {df['close_price'].min():.2f} – {df['close_price'].max():.2f}")
print(f"  Event Flags      : {df['event_flag'].value_counts().to_dict()}")
print()
print("  Final column dtypes:")
print(df.dtypes.to_string())
print()


# ─────────────────────────────────────────────
# STEP 15 — EXPORT CLEANED FILE
# ─────────────────────────────────────────────

output_path = "hdfc_bank_final_cleaned.csv"
df.to_csv(output_path, index=False)
print("=" * 60)
print(f"  ✅ Cleaned data saved to: {output_path}")
print("=" * 60)
