# Superstore Dataset — Exploratory Data Analysis

A Python-based exploratory data analysis (EDA) of the [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final), covering 9,994 retail orders placed across the United States between 2014 and 2017.

---

## 📁 Project Structure

```
.
├── superstore.csv          # Source dataset (download from Kaggle)
├── superstore_analysis.py  # Main EDA script
└── README.md
```

---

## 📦 Requirements

- Python 3.8+
- pandas
- numpy

Install dependencies:

```bash
pip install pandas numpy
```

---

## 🗂️ Dataset Overview

| Property | Value |
|---|---|
| Source | [Kaggle — Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| Rows | 9,994 |
| Columns | 21 |
| Period | 2014 – 2017 |
| Null values | None |

**Column reference:**

| Column | Type | Description |
|---|---|---|
| Order ID | str | Unique order identifier |
| Order Date / Ship Date | datetime | Order and shipment dates |
| Ship Mode | str | Shipping method (Standard, First Class, etc.) |
| Customer ID / Name | str | Customer identifiers |
| Segment | str | Consumer, Corporate, Home Office |
| Region / State / City | str | Geographic dimensions |
| Category / Sub-Category | str | Product classification |
| Sales | float | Order revenue in USD |
| Quantity | int | Units ordered |
| Discount | float | Fractional discount applied (0.0 – 0.8) |
| Profit | float | Net profit in USD |

---

## 🚀 Usage

1. Download `Sample - Superstore.csv` from Kaggle and rename it to `superstore.csv`.
2. Place it in the same directory as the script.
3. Run the analysis:

```bash
python superstore_analysis.py
```

---

## 🔍 What the Script Does

### Step 1 — Data Exploration

- `data.head()` — prints the first 5 rows for a quick visual check
- `data.info()` — column names, data types, and null counts
- `data.describe()` — count, mean, std, min/max, and quartiles for all numerical columns

### Step 2 — Basic Statistics

- **Per-feature stats** — mean, median, mode, standard deviation, variance, skewness, and kurtosis for `Sales`, `Quantity`, `Discount`, and `Profit`
- **Correlation matrix** — Pearson correlations between all numerical features via `data.corr()`
- **Group-level aggregations:**
  - Average and total Sales & Profit by **Category**
  - Average Sales & Profit by **Customer Segment**
  - Average and total Profit by **Region**
  - Average Sales & Profit by **Discount Tier** (No / Low / Mid / High)

---

## 📊 Key Findings

### Summary Statistics

| Feature | Mean | Median | Std Dev | Skewness |
|---|---|---|---|---|
| Sales | $189.93 | $90.88 | 328.00 | +6.37 |
| Quantity | 7.58 | 8.00 | 4.03 | ≈ 0 |
| Discount | 0.12 | 0.00 | 0.17 | +1.74 |
| Profit | $12.15 | $3.19 | 82.19 | +5.55 |

Sales and Profit are both strongly right-skewed — a small number of high-value orders pull the mean well above the median.

### Correlation Matrix

| | Sales | Quantity | Discount | Profit |
|---|---|---|---|---|
| **Sales** | 1.000 | 0.010 | -0.016 | **+0.314** |
| **Quantity** | 0.010 | 1.000 | 0.004 | 0.010 |
| **Discount** | -0.016 | 0.004 | 1.000 | **-0.184** |
| **Profit** | 0.314 | 0.010 | -0.184 | 1.000 |

- **Sales → Profit (+0.31):** Moderate positive relationship — higher revenue generally means higher profit.
- **Discount → Profit (−0.18):** Discounting meaningfully erodes profitability.
- **Quantity** is essentially uncorrelated with all other features.

