USE sql_store;

SELECT * FROM order_items;
SELECT * FROM customers;
SELECT * FROM products;

SELECT SUM(quantity) AS quantity_out FROM order_items;

SELECT SUM(quantity) AS Total_Produk3_Out FROM order_items WHERE product_id=3;

-- Kalo null, gak ikut keitung.
SELECT Count(phone) AS customers FROM customers;

SELECT MAX(quantity) AS Max_out FROM order_items;
SELECT MIN(quantity) AS Min_out FROM order_items;

-- MENCARI UNIQUE VALUEs
SELECT DISTINCT(oi.product_id) AS productkeluar, p.name FROM order_items oi
JOIN products p on oi.product_id = p.product_id;

SELECT DISTInct(state) from customers;

SELECT AVG(unit_price) AS Rata2_Harga from order_items;

