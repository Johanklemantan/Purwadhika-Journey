CREATE DATABASE flask_mysql;

USE flask_mysql;

CREATE TABLE employee(
	id int AUTO_INCREMENT PRIMARY KEY,
    username varchar(20) UNIQUE,
    name varchar(20),
    gender enum('M', 'L'),
    married tinyint
);

INSERT INTO employee (username, name, gender, married)
VALUES ('danang123', 'danang', 'M', 1),
('mrdarto', 'darto', 'M', 1),
('sulele', 'sule', 'M', 1);

SELECT * FROM employee;

SELECT * FROM tips;
SELECT * FROM irin;
SELECT * from irin where register_time > '02/03/2017';

SELECT * FROM user_tab_new;
describe user_tab_new;
SELECT * from user_tab_new where register_time > '2017-03-02 00:00:00';

-- ALTER TABLE user_tab_new
-- ALTER COLUMN register_time date()
SELECT *, CAST(register_time AS DATE) AS hehe
from user_tab_new;
-- WHERE hehe > 2017-03-02;

SELECT * FROM kuis1
