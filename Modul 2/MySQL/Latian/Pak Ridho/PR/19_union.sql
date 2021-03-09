USE sql_store;

SELECT *, 'Active' AS order_status FROM orders WHERE order_date >= '2019-01-01'
UNION
SELECT *, 'Inactive' AS order_status FROM orders WHERE order_date < '2019-01-01';