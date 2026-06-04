from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def sector_donut():

    root = Path(__file__).resolve().parent.parent

    holdings = pd.read_csv(
        root / "data" / "raw" / "09_portfolio_holdings.csv"
    )

    sector = (
        holdings.groupby("sector")["weight_pct"]
        .sum()
    )

    plt.figure(figsize=(8,8))

    plt.pie(
        sector,
        labels=sector.index,
        wedgeprops=dict(width=0.4)
    )

    plt.title("Sector Allocation")

    plt.savefig(
        root / "reports" / "charts" / "sector_allocation.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()