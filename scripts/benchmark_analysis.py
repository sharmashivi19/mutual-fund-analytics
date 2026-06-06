import plotly.express as px
from pathlib import Path

def benchmark_chart(df):

    fig = px.line(
        df,
        x="date",
        y="nav",
        color="amfi_code"
    )

    charts = Path(
        "../reports/charts"
    )

    charts.mkdir(
        parents=True,
        exist_ok=True
    )

    fig.write_image(
        charts /
        "benchmark_comparison.png"
    )

    return fig