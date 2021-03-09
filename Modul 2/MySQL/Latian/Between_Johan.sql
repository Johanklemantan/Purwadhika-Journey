USE sql_store;
select * from customers;

select * from customers where points > 1000 AND points < 3000;

-- 1486 dan 2967 include juga
select * from customers where points between 1486 AND  2967;

-- Quiz
-- tampilkan dari tabel customer yang birth_date nya di antara tanggal 1 jan 1990 sampai 1 jan 2000
Select * from customers where birth_date between '1990-01-01' and '2000-01-01';
