import plotly.express as px
import pandas as pd


def monthly_sip_trend(tx):

    sip = tx[
        tx["transaction_type"] == "SIP"
    ]

    sip["month"] = sip["transaction_date"].dt.to_period("M")

    monthly = (
    sip.groupby("month")["amount_inr"]
    .sum()
    .reset_index())

    monthly["month"] = monthly["month"].astype(str)

    fig = px.line(
    monthly,
    x="month",
    y="amount_inr",
    title="Monthly SIP Trend")

    fig.write_image(
        "../reports/charts/sip_trend.png"
    )

    return fig