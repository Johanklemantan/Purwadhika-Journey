USE sql_store;

SELECT * FROM customers WHERE points >= 1000 AND points <= 3000;

SELECT * FROM customers WHERE points BETWEEN 1486 AND 2967;  -- Include

-- tampilkan dari tabel customer, yang birth_date nya di antara tanggal 1 januari 1990 sampai 1 januari 2000
SELECT *
FROM customers
WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01';