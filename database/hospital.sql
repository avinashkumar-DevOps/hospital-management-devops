CREATE DATABASE hospital;

USE hospital;

CREATE TABLE patients (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
age INT,
gender VARCHAR(10),
contact VARCHAR(20)
);

CREATE TABLE doctors (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
specialization VARCHAR(100)
);

CREATE TABLE appointments (
id INT AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
date DATE
);

CREATE TABLE medicines (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
quantity INT,
price FLOAT
);

CREATE TABLE billing (
id INT AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
total_amount FLOAT
);