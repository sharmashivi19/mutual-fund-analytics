import pandas as pd

def clean_transactions():

    tx = pd.read_csv("data/raw/08_investor_transactions.csv")

    # Standardize transaction types
    mapping = {
        "sip": "SIP",
        "systematic investment plan": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "redemption": "Redemption",
        "redeem": "Redemption"
    }

    tx["transaction_type"] = (
        tx["transaction_type"]
        .astype(str)
        .str.lower()
        .str.strip()
        .replace(mapping)
    )

    # Fix dates
    tx["transaction_date"] = pd.to_datetime(
        tx["transaction_date"],
        errors="coerce"
    )

    # Validate amount
    tx["amount_inr"] = pd.to_numeric(
        tx["amount_inr"],
        errors="coerce"
    )

    tx = tx[tx["amount_inr"] > 0]

    # Validate KYC
    valid_kyc = ["Verified", "Pending", "Rejected"]

    invalid_kyc = tx[
        ~tx["kyc_status"].isin(valid_kyc)
    ]

    print("Invalid KYC rows:", len(invalid_kyc))

    # Save
    tx.to_csv(
        "data/processed/investor_transactions_clean.csv",
        index=False
    )

    print("Cleaning completed successfully!")