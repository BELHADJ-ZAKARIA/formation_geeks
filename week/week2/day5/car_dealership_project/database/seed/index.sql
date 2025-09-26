-- Drop tables if they exist to start with a clean slate.
-- The CASCADE option will also drop any dependent objects (like constraints).
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS salespeople;
DROP TABLE IF EXISTS customers;

-- -----------------------------------------------------
-- Table `vehicles`
-- Stores information about each car in the dealership.
-- -----------------------------------------------------
CREATE TABLE vehicles (
  id SERIAL PRIMARY KEY,
  vin VARCHAR(17) UNIQUE NOT NULL,
  make VARCHAR(50) NOT NULL,
  model VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  price NUMERIC(10, 2) NOT NULL,
  color VARCHAR(30)
);

-- -----------------------------------------------------
-- Table `salespeople`
-- Stores information about the sales staff.
-- -----------------------------------------------------
CREATE TABLE salespeople (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

-- -----------------------------------------------------
-- Table `customers`
-- Stores information about the people who buy cars.
-- -----------------------------------------------------
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20) UNIQUE
);

-- -----------------------------------------------------
-- Table `sales`
-- A relationship table that records each transaction,
-- linking a vehicle, a salesperson, and a customer.
-- -----------------------------------------------------
CREATE TABLE sales (
  id SERIAL PRIMARY KEY,
  vehicle_id INT NOT NULL,
  salesperson_id INT NOT NULL,
  customer_id INT NOT NULL,
  sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
  sale_price NUMERIC(10, 2) NOT NULL,
  CONSTRAINT fk_vehicle
    FOREIGN KEY(vehicle_id) 
    REFERENCES vehicles(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_salesperson
    FOREIGN KEY(salesperson_id) 
    REFERENCES salespeople(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_customer
    FOREIGN KEY(customer_id) 
    REFERENCES customers(id)
    ON DELETE CASCADE
);

-- -----------------------------------------------------
-- SEED DATA
-- Populate the tables with some sample records.
-- -----------------------------------------------------

-- Insert Sample Vehicles
INSERT INTO vehicles (vin, make, model, year, price, color) VALUES
('1G1FY1EJOA1234567', 'Toyota', 'Camry', 2022, 25000.00, 'Silver'),
('2G1FW1EJOA7654321', 'Honda', 'Civic', 2023, 22000.00, 'Black'),
('3G1FY1EJOA1122334', 'Ford', 'F-150', 2021, 45000.00, 'Red'),
('1G1FY2EJOA5566778', 'Chevrolet', 'Silverado', 2022, 48000.00, 'Blue'),
('2G1FW2EJOA9988776', 'Nissan', 'Altima', 2023, 24000.00, 'White'),
('3G1FY3EJOA1212121', 'Jeep', 'Wrangler', 2022, 35000.00, 'Green'),
('1G1FY4EJOA3434343', 'Hyundai', 'Sonata', 2023, 26000.00, 'Gray'),
('2G1FW3EJOA5656565', 'Kia', 'Sorento', 2021, 29000.00, 'Silver'),
('3G1FY5EJOA7878787', 'Subaru', 'Outback', 2022, 32000.00, 'Blue'),
('1G1FY6EJOA9090909', 'Mazda', 'CX-5', 2023, 28000.00, 'Red'),
('JTMDE78D93UD783HD', 'Tesla', 'Model 3', 2023, 42000.00, 'White'),
('YHS83UD92JD92HD83', 'BMW', 'X5', 2022, 65000.00, 'Black');

-- Insert Sample Salespeople
INSERT INTO salespeople (name, email) VALUES
('Alice Johnson', 'alice.j@cardealz.com'),
('Bob Smith', 'bob.s@cardealz.com'),
('Charlie Brown', 'charlie.b@cardealz.com'),
('Diana Prince', 'diana.p@cardealz.com'),
('Ethan Hunt', 'ethan.h@cardealz.com');

-- Insert Sample Customers
INSERT INTO customers (name, phone_number) VALUES
('Zack Snyder', '555-0101'),
('Patty Jenkins', '555-0102'),
('James Wan', '555-0103'),
('David Sandberg', '555-0104'),
('Andy Muschietti', '555-0105'),
('Cathy Yan', '555-0106'),
('James Gunn', '555-0107'),
('Matt Reeves', '555-0108'),
('Jaume Collet-Serra', '555-0109'),
('Angel Manuel Soto', '555-0110');

-- Insert Sample Sales
-- Linking vehicles, salespeople, and customers
INSERT INTO sales (vehicle_id, salesperson_id, customer_id, sale_date, sale_price) VALUES
(1, 1, 3, '2023-10-05', 24500.00),
(3, 2, 1, '2023-10-12', 44000.00),
(5, 1, 2, '2023-10-15', 23800.00),
(2, 3, 5, '2023-10-20', 21500.00),
(7, 4, 4, '2023-11-01', 25500.00),
(8, 5, 7, '2023-11-05', 28500.00),
(10, 2, 6, '2023-11-10', 27500.00),
(12, 4, 8, '2023-11-12', 64000.00);