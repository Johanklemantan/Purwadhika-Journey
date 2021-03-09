USE sql_store;

SELECT * FROM customers LIMIT 4;

SELECT * FROM customers LIMIT 3, 4;
-- LIMIT {digit1}, {digit2} berarti kita melompati data sebanyak {digit1}, lalu ambil {digit2} data setelahnya.

-- dari table customers tampilkan 3 data customer yang memiliki point terbesar
SELECT *
FROM customers
ORDER BY points DESC
LIMIT 3;