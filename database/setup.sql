CREATE DATABASE water_quality;
USE water_quality;

CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ph FLOAT,
    turbidity FLOAT,
    temperature FLOAT,
    tds FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
