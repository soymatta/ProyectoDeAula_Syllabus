CREATE DATABASE IF NOT EXISTS syllabus;
USE syllabus;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    role ENUM('admin', 'teacher') NOT NULL,
    status BOOLEAN NOT NULL,
    subjects VARCHAR(1500),
    faculties VARCHAR(1000),
    description VARCHAR(3000),
    image VARCHAR(500),
    weekly_hours INT,
    last_update DATETIME,
    micro_curriculum VARCHAR(5000)
);
CREATE TABLE IF NOT EXISTS subjects(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    faculties VARCHAR(300),
    teachers VARCHAR(5000),
    categories ENUM('practica', 'teorica', 'teorico-practica') NOT NULL,
    credits INT NOT NULL,
    weekly_hours INT,
    status BOOLEAN NOT NULL,
    bibliography VARCHAR(3000),
    content VARCHAR(50000) NOT NULL,
    faculty_id INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculties(id)
);
CREATE TABLE IF NOT EXISTS faculties(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    subjects VARCHAR(15000),
    teachers VARCHAR(5000),
    schema VARCHAR(5000)
);