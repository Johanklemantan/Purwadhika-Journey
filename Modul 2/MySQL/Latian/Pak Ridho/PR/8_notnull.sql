USE sql_store;

SELECT * FROM customers WHERE phone IS NOT NULL;

SELECT * FROM customers WHERE NOT (points > 1000);

-- tampilkan data yang shipped date nya tidak null
SELECT *
FROM orders
WHERE shipped_date IS NOT NULL