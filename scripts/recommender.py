def recommend_funds(
    perf,
    risk="Moderate"
):

    filtered = perf[
        perf["risk_grade"] == risk
    ]

    return (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )