import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

tx = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)



with engine.connect() as conn:

    source_rows = len(nav)

    db_rows = conn.execute(
        text("SELECT COUNT(*) FROM fact_nav")
    ).scalar()

    print(
        source_rows,
        db_rows
    )

    assert source_rows == db_rows