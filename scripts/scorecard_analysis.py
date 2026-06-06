import pandas as pd

def build_scorecard(
    cagr,
    sharpe,
    alpha,
    drawdown
):

    score = (
        cagr
        .merge(sharpe)
        .merge(alpha)
        .merge(drawdown)
    )

    score["return_rank"] = (
        score["cagr"]
        .rank(
            pct=True
        )
    )

    score["sharpe_rank"] = (
        score["sharpe"]
        .rank(
            pct=True
        )
    )

    score["alpha_rank"] = (
        score["alpha"]
        .rank(
            pct=True
        )
    )

    score["dd_rank"] = (
        (-score["max_drawdown"])
        .rank(
            pct=True
        )
    )

    score["score"] = (
        score["return_rank"]*30
        +
        score["sharpe_rank"]*25
        +
        score["alpha_rank"]*20
        +
        score["dd_rank"]*10
    )

    return score