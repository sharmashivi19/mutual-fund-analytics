import pandas as pd
import numpy as np

RF = 0.065

def sharpe_ratio(nav):

    rows = []

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ]

        returns = (
            df["daily_return"]
            .dropna()
        )

        sharpe = (
            (
                returns.mean()*252
                - RF
            )
            /
            (
                returns.std()
                * np.sqrt(252)
            )
        )

        rows.append(
            [fund, sharpe]
        )

    return pd.DataFrame(
        rows,
        columns=[
            "amfi_code",
            "sharpe"
        ]
    )
def sortino_ratio(nav):

    rows = []

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ]

        returns = (
            df["daily_return"]
            .dropna()
        )

        downside = (
            returns[
                returns < 0
            ]
        )

        sortino = (
            (
                returns.mean()*252
                - RF
            )
            /
            (
                downside.std()
                * np.sqrt(252)
            )
        )

        rows.append(
            [fund, sortino]
        )

    return pd.DataFrame(
        rows,
        columns=[
            "amfi_code",
            "sortino"
        ]
    )
def max_drawdown(nav):

    rows = []

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ].copy()

        df["running_max"] = (
            df["nav"]
            .cummax()
        )

        df["drawdown"] = (
            df["nav"]
            /
            df["running_max"]
            - 1
        )

        rows.append([
            fund,
            df["drawdown"].min()
        ])

    return pd.DataFrame(
        rows,
        columns=[
            "amfi_code",
            "max_drawdown"
        ]
    )