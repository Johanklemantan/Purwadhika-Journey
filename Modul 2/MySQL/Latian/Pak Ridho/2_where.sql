-- > greater than
-- >= greater than or equal
-- < smaller than
-- <= smaller than or equal
-- = equal
-- != not equal
-- <> not equal

USE sql_store;

SELECT * FROM customers WHERE state = 'VA';

SELECT * FROM customers WHERE state != 'VA';

SELECT * FROM customers WHERE state <> 'va';

SELECT * FROM customers WHERE birth_date > '1990-01-01';

-- Tampilkan data dari tabel orders, yang order_date nya lebih atau sama dengan dari tanggal 1 januari 2019
SELECT *
FROM orders
WHERE order_date >= '2019-01-01'