create database tops;

use tops;

create table student(
	id int,
    name varchar(20),
    email varchar(20)
    );
    
select* from student


create table employee (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contact_no VARCHAR(15),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    date_of_join DATE
	);
    
INSERT INTO employee (id, name, email, contact_no, department, salary, date_of_join) VALUES(
(1, 'Aarav Sharma', 'aarav.sharma@example.com', '9876543210', 'HR', 45000, '2021-03-15'),
(2, 'Priya Singh', 'priya.singh@example.com', '9123456780', 'Finance', 52000, '2020-11-20'),
(3, 'Rohan Patel', 'rohan.patel@example.com', '9812345678', 'IT', 68000, '2019-06-10'),
(4, 'Neha Gupta', 'neha.gupta@example.com', '9900123456', 'Marketing', 47000, '2022-01-05'),
(5, 'Aditya Verma', 'aditya.verma@example.com', '9876012345', 'IT', 72000, '2018-09-18'),
(6, 'Simran Kaur', 'simran.kaur@example.com', '9765432109', 'Sales', 43000, '2021-07-22'),
(7, 'Karan Mehta', 'karan.mehta@example.com', '9988776655', 'Finance', 56000, '2020-12-10'),
(8, 'Ishita Roy', 'ishita.roy@example.com', '9090909090', 'HR', 48000, '2023-02-14'),
(9, 'Manish Yadav', 'manish.yadav@example.com', '9356781234', 'Operations', 51000, '2019-03-30'),
(10, 'Sakshi Nair', 'sakshi.nair@example.com', '9001234567', 'IT', 67000, '2022-05-19'),
(11, 'Vihaan Joshi', 'vihaan.joshi@example.com', '7890123456', 'Marketing', 46000, '2020-08-25'),
(12, 'Ananya Desai', 'ananya.desai@example.com', '9123098765', 'Sales', 42000, '2021-04-11'),
(13, 'Harsh Kumar', 'harsh.kumar@example.com', '9988001122', 'Finance', 58000, '2018-12-02'),
(14, 'Kavya Menon', 'kavya.menon@example.com', '9654321876', 'HR', 44000, '2022-09-01'),
(15, 'Rajat Sinha', 'rajat.sinha@example.com', '9876501234', 'IT', 70000, '2019-07-17'),
(16, 'Divya Reddy', 'divya.reddy@example.com', '9012345600', 'Admin', 39000, '2023-01-28'),
(17, 'Arjun Malhotra', 'arjun.malhotra@example.com', '9823456781', 'Operations', 53000, '2017-11-14'),
(18, 'Meera Pandey', 'meera.pandey@example.com', '9009876543', 'Marketing', 47500, '2021-10-07'),
(19, 'Siddharth Rao', 'siddharth.rao@example.com', '9555012345', 'IT', 69000, '2020-03-11'),
(20, 'Aisha Sheikh', 'aisha.sheikh@example.com', '9800123456', 'Sales', 41000, '2022-06-09'),
(21, 'Varun Kapoor', 'varun.kapoor@example.com', '9201234567', 'Finance', 59000, '2019-10-22'),
(22, 'Sneha Kulkarni', 'sneha.kulkarni@example.com', '9900987654', 'Admin', 40000, '2021-02-18'),
(23, 'Mohit Chauhan', 'mohit.chauhan@example.com', '9875678901', 'IT', 73000, '2018-08-03'),
(24, 'Tanya Shah', 'tanya.shah@example.com', '9655012345', 'HR', 46000, '2020-07-27'),
(25, 'Parth Trivedi', 'parth.trivedi@example.com', 'parth.trivedi@example.com', '9345678901', 'Marketing', 48000, '2023-04-12')
);

