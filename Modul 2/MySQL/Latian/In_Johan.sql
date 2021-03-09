USE sql_store;

select * from customers;

select * from customers where state in ('VA','ca','il','tx','fl');

select * from customers where state not in ('VA','ca','il','tx','fl');

-- Quiz lagi
select * from products;

select * from products where quantity_in_stock in (49,38,72);