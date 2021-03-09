use sql_store;

SELECT * FROM customers;
-- Auto increment itu maksudnya gausa diisi. Nanti yang baru auto +1 sendiri (misal customer ID)
-- DEfault 0 artinya kalo gak diisi 0 (contohnya point)
-- Null YES (Gaboleh dikosongin) NO (BOleh dikosongin)
DESC customers;

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state)
VALUES('Robert', 'Pattinson','1992-02-29', '404-234-2222', '255 Avenue','Los Angeles','CA');

INSERT INTO customers(first_name, last_name, birth_date, phone, address, city, state, points)
VALUES('Andi', 'Warhol','1991-02-28', '403-234-2222', '254 Avenue','Detroit','NV','203'),
('Baliho', 'Tompel','1951-02-28', '666-666-6666', 'Jalan Sampang Avenue','Cilacap','JT','-10');

SELECT * FROM customers;

-- Insert Hierarchical Rows
SELECT * FROM orders;

DESC orders;

INSERT INTO orders(customer_id, order_date, status)
VALUES(1, '2019-02-04',1);

SELECT * from orders;

SELECT last_insert_id();
DESC order_items;

INSERT INTO order_items
VALUES
-- (last_insert_id(),1,19,2.95) 
(last_insert_id(),2,1,3.95);

SELECT last_insert_id();

SELECT * FROM order_items;

SELECT * FROM customers;
SELECT last_insert_id();

INSERT INTO customers(customer_id,first_name, last_name, birth_date, phone, address, city, state, points)
VALUES(18,'Roberty', 'Pattinsony','1992-02-29', '404-234-2222', '255 Avenue','Los Angeles','CA','20');

-- LAST INSERT ID BAKAL mereturn nilai terakhir yang pakai auto increment.