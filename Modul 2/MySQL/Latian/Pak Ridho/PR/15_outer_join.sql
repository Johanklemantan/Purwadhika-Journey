USE sql_store;

SELECT * FROM customers c RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN = menampilkan data berdasarkan tabel di sebelah kanan

SELECT c.customer_id, c.first_name, o.order_id FROM customers c JOIN orders o
ON c.customer_id = o.customer_id;

SELECT c.customer_id, c.first_name, o.order_id FROM orders o LEFT JOIN customers c
ON c.customer_id = o.customer_id;

-- LEFT JOIN = menampilkan data berdasarkan tabel di sebelah kiri, meskipun data di sebelah kanan tidak tersedia

-- IMPLICIT JOIN
SELECT * FROM customers c, orders o WHERE c.customer_id = o.customer_id;

-- EXERCISE
-- gabungkan antara tabel product dan tabel order_id dan tampilkan
-- semua product id dan product name
-- meskipun quantity nya null
SELECT p.product_id, p.name, oi.quantity
FROM products p
LEFT JOIN order_items oi
ON p.product_id = oi.product_id;
