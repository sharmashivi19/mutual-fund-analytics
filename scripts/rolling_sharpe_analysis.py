import numpy as np
import plotly.express as px
from pathlib import Path
import pandas as pd

def rolling_sharpe(nav):

    funds = nav["amfi_code"].unique()[:5]

    charts = []

    for fund in funds:

        df = nav[
            nav["amfi_code"] == fund
        ].copy()

        df["return"] = (
            df["nav"]
            .pct_change()
        )

        df["rolling_sharpe"] = (
            df["return"]
            .rolling(90)
            .mean()
            /
            df["return"]
            .rolling(90)
            .std()
        ) * np.sqrt(252)

        charts.append(df)

    final = pd.concat(charts)

    fig = px.line(
        final,
        x="date",
        y="rolling_sharpe",
        color="amfi_code",
        title="90 Day Rolling Sharpe"
    )

    output = Path("../reports/charts")
    output.mkdir(parents=True, exist_ok=True)

    fig.write_image(
        output / "rolling_sharpe_chart.png"
    )

    return fig