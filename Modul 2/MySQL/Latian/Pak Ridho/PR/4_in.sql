USE sql_store;

SELECT * FROM customers WHERE state IN ('VA', 'CA', 'IL', 'TX', 'FL');

SELECT * FROM customers WHERE state NOT IN ('VA', 'CA', 'IL', 'TX', 'FL');

-- tampilkan dari tabel products, data yang stocknya antara 49 / 38 / 72
-- tampilkan dari tabel products, data yang stocknya antara 49 / 38 / 72
SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72);