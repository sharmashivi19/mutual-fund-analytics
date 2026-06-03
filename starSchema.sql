CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE,
    fund_name TEXT,
    category TEXT,
    fund_house TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(fund_id)
        REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    investor_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    FOREIGN KEY(fund_id)
        REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    returns_1y REAL,
    returns_3y REAL,
    returns_5y REAL,
    expense_ratio REAL,
    FOREIGN KEY(fund_id)
        REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    aum REAL,
    FOREIGN KEY(fund_id)
        REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);