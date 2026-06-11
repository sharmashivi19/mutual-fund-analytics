import pandas as pd

def cohort_analysis(tx):

    tx["cohort_year"] = (
        tx.groupby("investor_id")
        ["transaction_date"]
        .transform("min")
        .dt.year
    )

    summary = (
        tx.groupby("cohort_year")
        .agg(
            avg_sip=("amount_inr","mean"),
            total_invested=("amount_inr","sum")
        )
        .reset_index()
    )

    return summary