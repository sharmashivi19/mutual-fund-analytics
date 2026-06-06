from scipy.stats import linregress
import pandas as pd

def alpha_beta(nav, benchmark):

    rows = []

    benchmark["benchmark_return"] = (
        benchmark["close"]
        .pct_change()
    )
    nav["date"] = pd.to_datetime(nav["date"]).dt.normalize()
    benchmark["date"] = pd.to_datetime(
    benchmark["date"]).dt.normalize()
    
    print(nav["date"].dtype)
    print(benchmark["date"].dtype)

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ]

        merged = pd.merge(
            df,
            benchmark,
            on="date"
        )

        print(f"Fund {fund}")
        print("Merged rows:", len(merged))
        print(merged.head())
        print("NAV range:")
        print(nav["date"].min(), nav["date"].max())

        print("\nBenchmark range:")
        print(benchmark["date"].min(), benchmark["date"].max())
        

        slope, intercept, _, _, _ = (
            linregress(
                merged["benchmark_return"].dropna(),
                merged["daily_return"].dropna()
            )
        )

        rows.append([
            fund,
            intercept*252,
            slope
        ])

    return pd.DataFrame(
        rows,
        columns=[
            "amfi_code",
            "alpha",
            "beta"
        ]
    )