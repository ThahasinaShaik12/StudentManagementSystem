show databases;
create database student_management;
use student_management;
create table students (
	id int auto_increment primary key,
    name varchar(100),
    age int,
    course varchar(100)
);
insert into students values(2,"thanuja",20,"it");
insert into students values(1,"thahasin",19,"it");
show tables;
select * from students;

