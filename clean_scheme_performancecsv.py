import pandas as pd

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("\nColumns:")
print(perf.columns.tolist())

print("\nFirst 5 rows:")
print(perf.head())

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio range
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    | (perf["expense_ratio_pct"] > 2.5)
]

print("Expense ratio anomalies:")
print(anomalies)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)
