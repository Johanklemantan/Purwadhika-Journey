USE sql_store;

-- RIGHT JOIN = menampilkan data berdasarkan tabel di sebelah kanan (gaboleh ada null)
-- LEFT JOIN = tampilkan data disebelah kiri meskipun data di sebelah kanan tidak cocok (ada yang null)
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM customers c RIGHT JOIN orders o
ON c.customer_id = o.customer_id;
-- SAMA AJA
SELECT * FROM customers c JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT c.customer_id, c.first_name, o.order_id FROM customers c JOIN orders o
ON c.customer_id = o.customer_id;

-- HATI2 BEDA HASILNYA
SELECT c.customer_id, c.first_name, o.order_id FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id;
-- BEDA SAMA INI
SELECT c.customer_id, c.first_name, o.order_id FROM orders o LEFT JOIN customers c
ON c.customer_id = o.customer_id;


-- IMPLICIT JOIN (RADA BAHAYA)
SELECT * FROM customers c, orders o 
WHERE c.customer_id = o.customer_id;


-- QUIZ

SELECT * FROM order_items;
SELECT * FROM products;
SELECT p.product_id, name, quantity FROM products p LEFT JOIN order_items oi
ON oi.product_id = p.product_id;
-- ORDER by product_id; 
