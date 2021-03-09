-- persen menunjukan berapapun jumlah karakter setelah kata yg ingin kita cari 
SELECT * FROM customers WHERE last_name LIKE 'brush%';

SELECT * FROM customers WHERE last_name LIKE '%b%';

SELECT * FROM customers WHERE last_name LIKE '%Y';

-- 1 UNDERSCORE mewakili 1 alphabet 
SELECT * FROM customers WHERE last_name LIKE '_____y';

SELECT * FROM customers WHERE last_name LIKE 'B____Y';

-- tampilkan data dari table customers yang alamatnya mengandung kata TRAIL atau AVENUE. Namun phone nya TIDAK ADA angka 8.
SELECT * FROM customers WHERE (address LIKE '%trail%' OR address LIKE '%avenue%') AND phone NOT LIKE '%8%';


