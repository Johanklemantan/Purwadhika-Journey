USE sql_store;

SELECT * FROM orders;

SELECT * FROM orders o JOIN customers c ON o.customer_id=c.customer_id;

SELECT order_id,order_date,c.customer_id,c.first_name,c.last_name
 FROM orders o JOIN customers c ON o.customer_id=c.customer_id;
 
 SELECT * FROM order_statuses;
 SELECT * FROM orders;
 
 SELECT order_id,order_date,c.customer_id,c.first_name,c.last_name, o.status, os.name as statusname
 FROM orders o JOIN customers c ON o.customer_id=c.customer_id
 JOIN order_statuses os ON o.status = os.order_status_id;
 
 SELECT * FROM order_statuses;
 
 -- Join join aja tergantung permintaan boss dan pake guidance dari EER diagram
SELECT o.order_id, c.customer_id, first_name, last_name, order_date, p.name AS produk, oi.quantity, os.name AS status, s.name AS shipper FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_statuses os ON o.status = os.order_status_id
LEFT JOIN shippers s ON o.shipper_id = s.shipper_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY order_id;



 CREATE TABLE  report_2des AS SELECT order_id,order_date,c.customer_id,c.first_name,c.last_name, o.status, os.name as statusname
 FROM orders o JOIN customers c ON o.customer_id=c.customer_id
 JOIN order_statuses os ON o.status = os.order_status_id;

SELECT * FROM report_2des;

DESC report_2des;

SELECT * FROM order_items;
DESC order_items;