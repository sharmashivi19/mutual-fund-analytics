-- Top 5 Funds by AUM

SELECT fund_id,
       SUM(aum) total_aum
FROM fact_aum
GROUP BY fund_id
ORDER BY total_aum DESC
LIMIT 5;
-- Average NAV per Month
SELECT
    month,
    AVG(nav)
FROM fact_nav n
JOIN dim_date d
ON n.date_id=d.date_id
GROUP BY month;
-- SIP YoY Growth
SELECT
    year,
    SUM(amount)
FROM fact_transactions t
JOIN dim_date d
ON t.date_id=d.date_id
WHERE transaction_type='SIP'
GROUP BY year;
-- Transactions by State
SELECT
    state,
    SUM(amount)
FROM fact_transactions
GROUP BY state;
-- Funds with Expense Ratio <1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;
-- Top Performing Fund (1Y)
SELECT *
FROM fact_performance
ORDER BY returns_1y DESC
LIMIT 1;
-- Average Expense Ratio
SELECT AVG(expense_ratio)
FROM fact_performance;
-- Monthly Transaction Volume
SELECT
    month,
    COUNT(*)
FROM fact_transactions t
JOIN dim_date d
ON t.date_id=d.date_id
GROUP BY month;
-- Highest NAV Fund
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;
-- Redemption Amount by Year
SELECT
    year,
    SUM(amount)
FROM fact_transactions t
JOIN dim_date d
ON t.date_id=d.date_id
WHERE transaction_type='Redemption'
GROUP BY year;