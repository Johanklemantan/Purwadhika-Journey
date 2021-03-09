USE sql_store;

SELECT * FROM customers ORDER BY first_name ASC;

SELECT * FROM customers ORDER BY first_name DESC;

SELECT * FROM customers ORDER BY state ASC;

SELECT * FROM customers ORDER BY birth_date;

-- dari tabel order_items, tampilkan semua data yang order id nya sama dengan 2, tampilkan pula data total pricenya.
-- lalu urutkan total price yang paling tinggi
SELECT *, quantity * unit_price AS total_price
FROM order_items
WHERE order_id = 2
ORDER BY total_price DESC;