import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_nav_trends(nav):

    fig = px.line(
        nav,
        x="date",
        y="nav",
        color="amfi_code",
        title="NAV Trends"
    )
    fig.write_image(
    "../reports/charts/nav_trend.png")

    return fig


def correlation_heatmap(nav):

    funds = nav["amfi_code"].unique()[:10]

    pivot = (
        nav[nav["amfi_code"].isin(funds)]
        .pivot(
            index="date",
            columns="amfi_code",
            values="nav"
        )
    )

    returns = pivot.pct_change()

    corr = returns.corr()

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("NAV Return Correlation Matrix")

    plt.savefig(
        "../reports/charts/correlation_heatmap.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()