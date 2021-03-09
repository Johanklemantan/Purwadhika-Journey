USE sql_store;

SELECT * FROM orders;

SELECT * FROM customers;

SELECT * FROM orders o JOIN customers c
ON o.customer_id = c.customer_id;

SELECT * FROM order_items;

SELECT * FROM products;


SELECT oi.order_id, p.product_id, p.name, oi.quantity FROM order_items oi JOIN products p
ON oi.product_id = p.product_id WHERE oi.order_id = 2;

SELECT oi.order_id FROM order_items oi;

-- tampilkan order_id, product_id, product name, quantity dan unit_price (gunakan unit price pada order items)
-- urutkan berdasarkan order_id dari order_id terkecil ke besar

SELECT *
FROM ORDER_ITEMS oi JOIN PRODUCTS p ON oi.product_id = p.product_id
ORDER BY order_id
