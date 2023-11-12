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
    image VARCHAR(500),
    last_update DATETIME
);
CREATE TABLE IF NOT EXISTS subjects(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    faculties VARCHAR(300),
    teachers VARCHAR(5000),
    type ENUM('practica', 'teorica', 'teorico-practica') NOT NULL,
    credits INT NOT NULL,
    bibliography VARCHAR(3000),
    content VARCHAR(50000) NOT NULL,
    faculty_id INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculties(id)
);
CREATE TABLE IF NOT EXISTS faculties(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    subjects VARCHAR(15000),
    teachers VARCHAR(5000)
);
CREATE TABLE IF NOT EXISTS syllabus(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    cycle VARCHAR(500),
    identification VARCHAR(10000),
    justification VARCHAR(10000),
    competences VARCHAR(10000),
    learning_results VARCHAR(10000),
    methodology VARCHAR(10000),
    program_content VARCHAR(10000),
    strategies VARCHAR(10000),
    evaluation VARCHAR(2500),
    bibliography VARCHAR(10000) subject_id INT NOT NULL,
    subject_id INT NOT NULL,
    faculty_id INT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (faculty_id) REFERENCES faculties(id)
);
CREATE TABLE IF NOT EXISTS versions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    update_date DATETIME NOT NULL,
    description VARCHAR(500),
    owner VARCHAR(100),
    user_id INT NOT NULL,
    FOREIGN KEY user_id REFERENCES users(id)
)