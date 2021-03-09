USE sql_store;

SELECT * FROM customers;

DESC customers;

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES('Robert', 'Pattinson', '1992-02-29', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

SELECT * FROM customers;

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES
('Andy', 'Warholl', '1991-02-28', '404-234-2222', '255 Avenue', 'Atlanta', 'GA'),
('Buzz', 'Lightyear', '1990-03-15', '404-234-2222', '255 Avenue', 'Visalia', 'CA'),
('Nemo', 'Fish', '1994-01-01', '404-234-2222', '255 Avenue', 'Visalia', 'CA');

SELECT * FROM customers;

-- Insert Hierarchical Rows
SELECT * FROM orders;

DESC order_items;

INSERT INTO orders(customer_id, order_date, status)
VALUES (3, '2019-02-05', 1);

SELECT * FROM orders;

SELECT LAST_INSERT_ID();

INSERT INTO order_items
VALUES
-- (last_insert_id(), 1, 10, 2.95),
-- (last_insert_id(), 2, 1, 3.95);
-- (11, 3, 2, 2.5);
(12, 3, 3, 4.5);

SELECT * FROM order_items;


SELECT * FROM order_items;

SELECT * FROM orders o JOIN order_items oi ON
o.order_id = oi.order_id
WHERE o.order_id = 11;

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES('Daniel', 'Enderson', '1992-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

select * from customers;

SELECT LAST_INSERT_ID();

SELECT * FROM customers;

INSERT INTO customers(customer_id, first_name, last_name, birth_date, phone, address, city, state)
VALUES(18, 'Andy', 'Andyan', '1994-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES('Budi', 'Budian', '1995-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

INSERT INTO customers(customer_id, first_name, last_name, birth_date, phone, address, city, state)
VALUES(22, 'Caca', 'Handika', '1996-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

INSERT INTO customers(customer_id, first_name, last_name, birth_date, phone, address, city, state)
VALUES(20, 'Dedi', 'Kobokan', '1996-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES('Edi', 'Brokoli', '1996-02-01', '404-234-2222', '255 Avenue', 'Los Angeles', 'LA');
