use sql_store;

select * from customers;

select * from order_items;

select * from orders;

select * from products;

SELECT order_id, o.customer_id, first_name, last_name FROM orders o JOIN customers c
ON o.customer_id=c.customer_id;

SELECT * FROM order_items oi JOIN products p
ON oi.product_id = p.product_id;

SELECT oi.order_id,p.product_id, name, quantity FROM order_items oi JOIN products p
ON oi.product_id = p.product_id where oi.order_id = 2;

SELECT * FROM orders o JOIN customers c
ON o.customer_id=c.customer_id Where first_name = 'Elka';

SELECT * From order_items;

SELECT order_id, oi.product_id, name, quantity, oi.unit_price FROM order_items oi JOIN products p
ON oi.product_id=p.product_id order by order_id;