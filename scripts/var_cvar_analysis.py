import pandas as pd
import numpy as np

def calculate_var_cvar(nav):

    rows = []

    for fund in nav["amfi_code"].unique():

        df = nav[
            nav["amfi_code"] == fund
        ].copy()

        returns = (
            df["nav"]
            .pct_change()
            .dropna()
        )

        var95 = np.percentile(
            returns,
            5
        )

        cvar95 = returns[
            returns <= var95
        ].mean()

        rows.append([
            fund,
            var95,
            cvar95
        ])

    return pd.DataFrame(
        rows,
        columns=[
            "amfi_code",
            "VaR_95",
            "CVaR_95"
        ]
    )