import pandas as pd

def sector_hhi(holdings):

    hhi = (
        holdings
        .groupby("amfi_code")
        ["weight_pct"]
        .apply(
            lambda x:
            (x/100).pow(2).sum()
        )
        .reset_index()
    )

    hhi.columns = [
        "amfi_code",
        "HHI"
    ]
    return hhi