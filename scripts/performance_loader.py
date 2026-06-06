import pandas as pd
from pathlib import Path

def load_data():

    root = Path(__file__).resolve().parent.parent

    nav = pd.read_csv(
        root / "data" / "processed" / "nav_history_clean.csv"
    )

    perf = pd.read_csv(
        root / "data" / "processed" / "scheme_performance_clean.csv"
    )

    nav["date"] = pd.to_datetime(nav["date"])

    return nav, perf