# Inventory-Database-System

A lightweight, terminal-based Inventory Management System built with **Python** and **MySQL**. This application allows users to manage stock levels, add new products, and track inventory health with built-in low-stock alerts.

## Features
* **Full CRUD functionality**: Create, Read, Update, and Delete products.
* **Input Validation**: Prevents crashes from invalid data types or non-existent IDs.
* **Low Stock Alerts**: Automatically flags items with fewer than 5 units.
* **Formatted Display**: Clean, table-style layout for terminal viewing.

---

## Prerequisites
Before running this project, ensure you have the following installed:
* [MySQL Server](https://dev.mysql.com/downloads/mysql/)
* [Python 3.x](https://www.python.org/)
* `mysql-connector-python` library

---

## ⚙️ Setup & Installation

### 1. Database Setup
Log into your MySQL terminal and run the following to initialize the database:
```sql
CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);