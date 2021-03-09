USE sql_store;
-- untuk panggil pake select. tiap akhir querry pake ;--
-- * artinya semua --
SELECT * FROM customers;
SELECT phone, city, state FROM customers;

SELECT first_name, last_name FROM customers;

SELECT first_name, last_name, points, (points+10)*100 as 'discount factor' FROM customers;
-- distinct untuk show unique value --
SELECT distinct(STATE) FROM customers;

-- QUIZ

SELECT * FROM products;

SELECT name, unit_price, (1.2* unit_price) as'new price' FROM products;
