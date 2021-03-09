USE sql_store;

select * from order_items;

SELECT * from sql_inventory.products;

SELECT * FROM order_items oi JOIN sql_inventory.products sqip ON sqip.product_id = oi.product_id;
SELECT * FROM order_items oi JOIN sql_inventory.products sqip ON oi.product_id = sqip.product_id;