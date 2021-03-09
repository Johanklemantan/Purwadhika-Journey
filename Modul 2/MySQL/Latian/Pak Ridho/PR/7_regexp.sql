USE sql_store;

SELECT * FROM customers WHERE last_name LIKE '%field';

SELECT * FROM customers WHERE last_name REGEXP 'field$';
-- tanda $ menandakan suatu kata adalah akhiran

SELECT * FROM customers WHERE last_name REGEXP '^B';
-- tanda ^ menandakan suatu kata atau karakter adalah awalan

SELECT * FROM customers WHERE last_name LIKE 'field%' OR last_name LIKE 'mac%' OR last_name LIKE 'rose%';

SELECT * FROM customers WHERE last_name REGEXP '^field|^mac|^rose';

SELECT * FROM customers WHERE last_name REGEXP '[gimd]e'; -- ge / ie / me / de

SELECT * FROM customers WHERE last_name REGEXP '[a-h]e'; -- [a sampai h] dipertemukan dengan execute

-- RECAP
-- ^ beginning / awalan
-- $ ending / akhiran
-- | logical OR
-- [abcd] list of char
-- [a-h] range of char

-- tampilkan data customers yang last names mengandung B diikuti dengan R atau U
SELECT * FROM customers WHERE last_name REGEXP 'B[RU]';
