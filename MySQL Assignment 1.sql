
-- 1. Table Creation (CREATE): Write the SQL statements to create a database named “employee” and the following tables based on the provided schema:
-- Departments
-- Location
--  Employees
create database employee;
use employee;

create table departments (
department_id int primary key,
department_name varchar(100));

create table location (
location_id int primary key,
location varchar(30));

CREATE TABLE employees (
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
gender ENUM('M', 'F'),
age INT,
hire_date DATE,
designation VARCHAR(100),
department_id INT,
location_id INT,
salary DECIMAL(10,2),
FOREIGN KEY (department_id) REFERENCES departments(department_id),
FOREIGN KEY (location_id) REFERENCES location(location_id));

-- 2. Table Alteration (ALTER): Consider the following scenarios and write the SQL statements to alter the structure of the tables accordingly:

-- Add a new column named "email" to the Employees table to store employee email addresses.
ALTER TABLE employees
ADD COLUMN email VARCHAR(100);

-- Modify the data type of the "designation" column in the Employees table to support a wider range of values.
ALTER TABLE employees
MODIFY COLUMN designation VARCHAR(255);

-- Drop the “age” column from the Employees table.
Alter table employees drop column age;

-- Rename the “hire_date” column to “date_of_joining”.
ALTER TABLE employees
RENAME COLUMN hire_date TO date_of_joining;

-- 3 Table Renaming (RENAME): Rewrite the SQL statements to rename the following tables:

-- Rename the "Departments" table to "Departments_Info".
alter table departments rename to Departments_Info;

-- Rename the "Location" table to "Locations".
alter table location rename to locations;

-- 4. Table Truncation (TRUNCATE): Write an SQL statement to truncate the Employees table.
TRUNCATE TABLE employees;

-- 5. Database & Table Dropping (DROP): Write the SQL statements to drop the Employees table and then the “employee” database.
drop table employees;
drop database employee;

-- 1. Database Recreation:
-- Drop the 'employee' database if it exists and recreate it using the provided schema, ensuring that all tables are created with the appropriate constraints as instructed.
drop database if exists employee;
create database employee;
use employee;

create table departments (
department_id int primary key auto_increment,
department_name varchar(100)
);
create table location (
location_id int primary key auto_increment,
location varchar(30));
CREATE TABLE employees (
employee_id INT PRIMARY KEY auto_increment,
employee_name VARCHAR(50),
gender ENUM('M', 'F'),
age INT,
hire_date DATE,
designation VARCHAR(100),
department_id INT,
location_id INT,
salary DECIMAL(10,2),
FOREIGN KEY (department_id) REFERENCES departments(department_id),
FOREIGN KEY (location_id) REFERENCES location(location_id));

-- 2. Departments Table:
-- Ensure that the "department_id" uniquely identifies each department.
alter table departments
add unique (department_id);

-- Set up constraints on the "department_name" to avoid duplicate and null entries.
alter table departments
modify department_name varchar(100) not null unique;
-- 3. Location Table:

-- Establish a mechanism to automatically generate unique identifiers for each location, ensuring that they are incremented sequentially.
alter table location
modify location varchar(30) not null;

-- Implement constraints to prevent the insertion of null and duplicate locations.
alter table location
add unique (location);

-- 4. Employees Table:

-- Guarantee that each employee has a distinct identifier.
alter table employees
add primary key (employee_id);
-- Create a restriction to ensure that the employee's name is always provided
alter table employees
modify employee_name varchar(50) not null;
-- Limit the acceptable values for the "gender" field to only 'M' or 'F'.
alter table employees
modify gender char(1) check (gender in ('M','F'));
-- Enforce a condition to ensure that the employee's age is 18 or above.
alter table employees
modify age int check (age >= 18);
-- Automatically assign the current date to the "hire_date" field if not specified.
alter table employees
modify hire_date date default (current_date);
-- Establish links between the "department_id" and "location_id" fields in the "employees" table and their respective tables.
alter table employees
add FOREIGN KEY (department_id) REFERENCES departments(department_id);
alter table employees
add FOREIGN KEY (location_id) REFERENCES location(location_id);











