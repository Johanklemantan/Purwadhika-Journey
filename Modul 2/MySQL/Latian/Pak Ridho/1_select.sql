USE sql_store;

-- CLAUSE 
SELECT * FROM customers;

SELECT first_name, last_name FROM customers;

SELECT first_name, last_name, points, (points+10)*100 as 'discount factor' FROM customers;

SELECT * FROM customers;

SELECT DISTINCT(state) FROM customers;

-- tampilkan dari tabel products name dan unit price, berikut dengan 1 kolom baru bernama 'new price' yg berisi 1.2 kali unit_price

SELECT name, unit_price, (unit_price)*1.2 as 'new price' FROM products;




