USE sql_store;

SELECT * FROM customers WHERE points > (SELECT AVG(points) FROM customers WHERE state = 'ca');

SELECT * FROM order_items oi JOIN products p ON oi.product_id = p.product_id
WHERE quantity = (SELECT MAX(quantity) FROM order_items);

SELECT * FROM order_items WHERE quantity = (SELECT MAX(quantity) FROM order_items);

-- tampilkan data order_id yang memesan product sebanyak 10
SELECT * FROM order_items WHERE order_id IN (SELECT order_id FROM order_items WHERE quantity=10) AND quantity = 10;
SELECT * FROM order_items WHERE order_id IN (SELECT order_id FROM order_items WHERE quantity=10) AND quantity = 10;

-- tampilkan data customer yang belum pernah melakukan order
SELECT * FROM customers WHERE customer_id NOT IN (SELECT DISTINCT(customer_id) from orders);
