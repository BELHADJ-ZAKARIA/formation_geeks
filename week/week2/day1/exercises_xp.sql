-- Exercise 1 : Items and customers

-- Create two tables items, customers
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR (60),
    item_price INTEGER
);

CREATE TABLE customers(
    customers_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL
);

-- Add the following items to the items table
INSERT INTO items(item_id, item_name, item_price)
VALUES (1, 'Small Desk', 100),
       (2, 'Large desk', 300),
       (3, 'Fan', 80);

-- Add 5 new customers to the customers table:
INSERT INTO customers(customers_id, first_name, last_name)
VALUES (1, 'Greg', 'Jones'),
       (2, 'Sandra', 'Jones'),
       (3, 'Scott', 'Scott'),
       (4, 'Trevor', 'Green'),
       (5, 'Melanie', 'Johnson');

-- All the items
SELECT * FROM items;

-- All the items with a price above 80 (80 not included)
SELECT * FROM items WHERE item_price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items WHERE item_price <= 300;

-- All customers whose last name is ‘Smith’
-- Outcome is No data because there's no customers with ‘Smith’ as last name 
SELECT * FROM customers WHERE last_name = 'Smith';

-- All customers whose last name is ‘Jones’
SELECT * FROM customers WHERE last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’
SELECT * FROM customers WHERE first_name != 'Scott';