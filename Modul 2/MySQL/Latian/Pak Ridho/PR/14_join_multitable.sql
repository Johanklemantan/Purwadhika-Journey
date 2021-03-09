USE sql_store;

SELECT o.order_id, c.customer_id, first_name, last_name, order_date, p.name, oi.quantity, os.name AS status, s.name AS shipper FROM orders o
JOIN order_statuses os ON o.status = os.order_status_id
JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN shippers s ON o.shipper_id = s.shipper_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
ORDER BY order_id;

SELECT * FROM order_statuses;

SELECT * FROM shippers;

SELECT * FROM orders;

DESC report_lengkap;

-- SELECT order_id, order_date, c.customer_id, c.first_name, c.last_name, o.status, os.name as status_name
-- FROM orders o JOIN customers c ON o.customer_id = c.customer_id
-- JOIN order_statuses os ON o.status = os.order_status_id;

-- Create Copy Table
-- CREATE TABLE report_2_des AS SELECT order_id, order_date, c.customer_id, c.first_name, c.last_name, o.status, os.name as status_name
-- FROM orders o JOIN customers c ON o.customer_id = c.customer_id
-- JOIN order_statuses os ON o.status = os.order_status_id;

select * from order_statuses;

SELECT * FROM report_2_des;