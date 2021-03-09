USE sql_store;

SELECT * FROM customers WHERE birth_date > '1990-01-01' AND points > 1000;
SELECT * FROM customers WHERE birth_date > '1990-01-01' OR points > 1000;

SELECT * FROM customers WHERE birth_date > '1990-01-01' OR points > 1000 AND state = 'VA'; -- AND > OR

SELECT * FROM customers WHERE birth_date > '1990-01-01' OR (points > 1000 AND state = 'VA');

SELECT * FROM customers WHERE (birth_date > '1990-01-01' OR points > 1000) AND state = 'VA';

SELECT * FROM customers WHERE NOT (birth_date > '1990-01-01' OR points > 1000);
-- NOT = negasi (< // >=) (> // <=) (= // !=) (OR // AND)
SELECT * FROM customers WHERE birth_date <= '1990-01-01' AND points <= 1000;

-- tampilkan data dari order_items yang total belanja nya lebih dari 30 dollar

SELECT *
FROM order_items
WHERE quantity*unit_price>30;