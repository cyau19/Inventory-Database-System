CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, quantity, price)
VALUES 
    ("Laptop", 10, 899.99),
    ("Keyboard", 25, 49.99),
    ("Wireless Mouse", 50, 29.99),
    ("Monitor", 3, 199.50);

SELECT * FROM products;

SELECT name, quantity 
FROM products 
WHERE quantity < 5;

SELECT SUM(quantity * price) AS total_inventory_value 
FROM products;

UPDATE products
SET quantity = quantity - 1
WHERE id = 1;