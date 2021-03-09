USE sql_store;
SELECT * FROM customers;

SELECT * FROM customers WHERE last_name LIKE '%field%';

-- tanda $ (dollar) menandakaan suatu kata adalah akhiran
SELECT * FROM customers WHERE last_name REGEXP 'field$';

-- tanda ^(petik) menandakan suatu kata yang diawali dengan B
SELECT * FROM customers WHERE last_name REGEXP '^b';

-- diawali dengan SEMUANYA
SELECT * FROM customers WHERE last_name LIKE 'Field%' or last_name LIKE 'mac%' or last_name LIKE 'rose%';

-- CObain pake REGEX
SELECT * FROM customers WHERE last_name REGEXP '^field|^mac|^rose';
-- maksudnya yang mengandung kata ge, ie, atau me
SELECT * FROM customers WHERE last_name REGEXP '[gim][e]';
-- pasang2in aja ge ie me gy iy my
SELECT * FROM customers WHERE last_name REGEXP '[gim][ey]';
-- a sampai h dipertemeukan dengan e
SELECT * FROM customers WHERE last_name REGEXP '[a-h]e';

-- RECAP REGEX YA

-- ^ awalan
-- $ ending
-- | logical OR
-- [abcd] list of char
-- [a-h] range of char
SELECT * FROM customers;

SELECT * FROM customers WHERE first_name REGEXP 'elka|ambur';

SELECT * FROM customers WHERE last_name REGEXP 'ey$|on$';

SELECT * FROM customers WHERE last_name REGEXP '^my|sE';

SELECT * FROM customers WHERE last_name REGEXP 'b[ru]';