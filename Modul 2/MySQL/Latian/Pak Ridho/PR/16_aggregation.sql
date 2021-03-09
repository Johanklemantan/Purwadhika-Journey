USE sql_store;

SELECT SUM(quantity) AS total_quantity_out FROM order_items;
SELECT SUM(quantity) AS total_id3_quantity_out FROM order_items WHERE product_id = 3;

SELECT COUNT(*) AS customers FROM customers;

SELECT COUNT(DISTINCT(state)) AS customers_state FROM customers;

SELECT MAX(quantity) AS max_out FROM order_items;
SELECT MIN(quantity) AS min_out FROM order_items;

SELECT DISTINCT(oi.product_id) AS product_out, p.name FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

SELECT DISTINCT(state) FROM customers;

SELECT AVG(unit_price) FROM order_items;


