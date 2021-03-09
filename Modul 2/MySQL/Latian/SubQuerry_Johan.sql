USE sql_store;

SELECT * FROM customers;
SELECT * FROM orders;

-- TANPA SUB QUERRY (HARUS 2x kerja)
SELECT avg(points) from customers;
SELECT avg(points) from customers WHERE state = 'Ca';

SELECT * FROM customers WHERE points > 1486;

-- PAKE SUB QUERRY
SELECT * FROM customers WHERE points > (SELECT avg(points) from customers WHERE state = 'ca');

SELECT * from order_items;

SELECT * FROM order_items WHERE quantity = (SELECT MAX(quantity) FROM order_items);

SELECT * FROM order_items WHERE order_id IN (SELECT order_id FROM order_items WHERE quantity=10);
SELECT order_id FROM order_items WHERE quantity=10;

-- Tampilkan data order ID yang memesan produk sebanyak 10.
SELECT * FROM order_items WHERE order_id IN (SELECT order_id FROM order_items WHERE quantity=10) AND quantity = 10;

SELECT * FROM order_items oi JOIN products p ON oi.product_id = p.product_id
WHERE quantity = (SELECT MAX(quantity) FROM order_items);

-- --SELECT * FROM customers c 
-- JOIN orders o on c.customer_id = o.customer_id
-- WHERE customer_id NOT IN orders;

-- Tampilkan customer yang belom pernah melakukan order.
SELECT * FROM customers WHERE customer_id NOT IN (SELECT Distinct customer_id from orders);

-- SELECT DISTINCT(customer_id) FROM orders;-- 