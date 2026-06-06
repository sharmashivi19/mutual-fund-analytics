import pandas as pd

def calculate_daily_returns(nav):

    nav = nav.sort_values(
        ["amfi_code", "date"]
    )

    nav["daily_return"] = (
        nav.groupby("amfi_code")["nav"]
        .pct_change()
    )

    return nav
def calculate_cagr(nav):

    results = []

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ].sort_values("date")

        start = df.iloc[0]["nav"]
        end = df.iloc[-1]["nav"]

        years = (
            df["date"].max()
            -
            df["date"].min()
        ).days / 365

        cagr = (
            (end/start)**(1/years)
        ) - 1

        results.append(
            [fund, cagr]
        )

    return pd.DataFrame(
        results,
        columns=[
            "amfi_code",
            "cagr"
        ]
    )