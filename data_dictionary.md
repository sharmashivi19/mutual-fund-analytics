# Mutual Fund Analytics Data Dictionary

## Source Files

| File Name | Description | Record Count |
|------------|------------|------------|
| nav_history_clean.csv | Historical NAV data for mutual fund schemes | 46,000 |
| investor_transactions_clean.csv | Investor transaction records | 32,778 |
| scheme_performance_clean.csv | Fund performance and risk metrics | 40 |

---

# 1. nav_history_clean.csv

## Business Purpose
Stores daily Net Asset Value (NAV) history for mutual fund schemes identified by AMFI code.

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| amfi_code | INTEGER | Unique AMFI scheme identifier | AMFI |
| date | DATE | NAV reporting date | AMFI |
| nav | FLOAT | Net Asset Value per unit on the specified date | AMFI |

### Business Rules

- `amfi_code` must exist in scheme master data.
- `date` must be a valid calendar date.
- `nav > 0`.
- Missing NAV values are forward-filled during data cleaning.

---

# 2. investor_transactions_clean.csv

## Business Purpose

Captures investor purchase, SIP, and redemption transactions across mutual fund schemes.

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| investor_id | VARCHAR(20) | Unique investor identifier | Internal Transaction System |
| transaction_date | DATE | Transaction execution date | Internal Transaction System |
| amfi_code | INTEGER | Mutual fund scheme identifier | AMFI |
| transaction_type | VARCHAR(20) | Transaction category (SIP, Lumpsum, Redemption) | Internal Transaction System |
| amount_inr | INTEGER | Transaction amount in Indian Rupees | Internal Transaction System |
| state | VARCHAR(100) | Investor state | KYC Records |
| city | VARCHAR(100) | Investor city | KYC Records |
| city_tier | VARCHAR(10) | Investor city classification (T30/B30) | Internal Classification |
| age_group | VARCHAR(20) | Investor age segment | Investor Profile |
| gender | VARCHAR(20) | Investor gender | Investor Profile |
| annual_income_lakh | FLOAT | Annual income in lakhs of INR | Investor Profile |
| payment_mode | VARCHAR(50) | Payment method used for transaction | Internal Transaction System |
| kyc_status | VARCHAR(20) | Investor KYC verification status | Compliance/KYC System |

### Business Rules

- `amount_inr > 0`
- `transaction_type` ∈ {SIP, Lumpsum, Redemption}
- `kyc_status` ∈ {Verified, Pending, Rejected}
- `transaction_date` must be a valid date
- Every transaction must map to a valid `amfi_code`

---

# 3. scheme_performance_clean.csv

## Business Purpose

Contains scheme-level performance, risk, and operational metrics used for analytics and reporting.

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| amfi_code | INTEGER | Unique scheme identifier | AMFI |
| scheme_name | VARCHAR(255) | Official scheme name | AMFI |
| fund_house | VARCHAR(255) | Asset Management Company (AMC) | AMFI |
| category | VARCHAR(100) | Mutual fund category | AMFI |
| plan | VARCHAR(20) | Plan type (Regular/Direct) | AMFI |
| return_1yr_pct | FLOAT | One-year annualized return (%) | Performance Dataset |
| return_3yr_pct | FLOAT | Three-year annualized return (%) | Performance Dataset |
| return_5yr_pct | FLOAT | Five-year annualized return (%) | Performance Dataset |
| benchmark_3yr_pct | FLOAT | Three-year benchmark return (%) | Benchmark Dataset |
| alpha | FLOAT | Risk-adjusted excess return metric | Performance Dataset |
| beta | FLOAT | Volatility relative to benchmark | Performance Dataset |
| sharpe_ratio | FLOAT | Risk-adjusted performance metric | Performance Dataset |
| sortino_ratio | FLOAT | Downside risk-adjusted return metric | Performance Dataset |
| std_dev_ann_pct | FLOAT | Annualized standard deviation (%) | Performance Dataset |
| max_drawdown_pct | FLOAT | Maximum decline from peak value (%) | Performance Dataset |
| aum_crore | INTEGER | Assets Under Management (₹ Crore) | AMC Reports |
| expense_ratio_pct | FLOAT | Annual expense ratio (%) | AMFI |
| morningstar_rating | INTEGER | Morningstar rating (1-5) | Morningstar |
| risk_grade | VARCHAR(50) | Scheme risk classification | Internal Risk Framework |

### Business Rules

- Return columns must be numeric.
- Expense ratio should typically be between 0.10% and 2.50%.
- Morningstar rating should be between 1 and 5.
- AUM must be non-negative.
- Alpha, Beta, Sharpe Ratio, and Sortino Ratio must be numeric.

---

# Key Relationships

## Scheme Key

`amfi_code`

Used to join:

- nav_history_clean.csv
- investor_transactions_clean.csv
- scheme_performance_clean.csv

Example:

```sql
SELECT *
FROM investor_transactions t
JOIN scheme_performance s
ON t.amfi_code = s.amfi_code;
```

---

# Data Quality Checks

## NAV Dataset

- No duplicate `(amfi_code, date)` combinations.
- NAV values must be positive.
- Dates sorted by scheme and date.

## Transactions Dataset

- Amounts greater than zero.
- Valid transaction types.
- Valid KYC status values.
- Valid transaction dates.

## Performance Dataset

- Numeric return metrics.
- Expense ratio anomaly checks.
- Valid Morningstar ratings.
- Non-null AMFI codes.

---

# Data Sources

| Source | Description |
|----------|----------|
| AMFI | Association of Mutual Funds in India |
| AMC Reports | Fund house disclosures and AUM reports |
| Investor KYC System | Customer verification records |
| Internal Transaction System | Investor purchase and redemption records |
| Morningstar | Independent fund ratings |