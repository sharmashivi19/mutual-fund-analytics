import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Parse dates
nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

# Remove duplicates
nav = nav.drop_duplicates()

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Forward fill NAV
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Validate NAV
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)
