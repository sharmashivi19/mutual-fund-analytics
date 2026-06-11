import pandas as pd

def sip_continuity(tx):

    sip = tx[
        tx["transaction_type"]=="SIP"
    ].copy()

    rows = []

    for inv in sip["investor_id"].unique():

        df = sip[
            sip["investor_id"] == inv
        ].sort_values(
            "transaction_date"
        )

        if len(df) < 6:
            continue

        avg_gap = (
            df["transaction_date"]
            .diff()
            .dt.days
            .mean()
        )

        risk = (
            "At Risk"
            if avg_gap > 35
            else "Healthy"
        )

        rows.append([
            inv,
            avg_gap,
            risk
        ])

    return pd.DataFrame(
        rows,
        columns=[
            "investor_id",
            "avg_gap_days",
            "status"
        ]
    )