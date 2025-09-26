-- Exercise 1: DVD Rental

-- 1.1. Find out how many films there are for each rating
SELECT rating, COUNT(*) FROM film GROUP BY rating;

-- 1.2. Get a list of all the movies that have a rating of G or PG-13
SELECT * FROM film WHERE rating IN ('G', 'PG-13');

/*
1.2.1. Filter this list further: look for only movies that are under 2 hours long,
and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
*/
SELECT * 
FROM 
    film 
WHERE 
    rating IN ('G', 'PG-13') 
    AND length < 120 
    AND  rental_rate < 3.00
ORDER BY
    title ASC;

-- 1.3. Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer
SET first_name= 'Zakaria', last_name= 'Belhadj', email='emailexample@gmail.com'
WHERE customer_id = 1;

-- 1.4. Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address
SET address = '123 Fake Street'
WHERE address_id = (
    SELECT address_id
    FROM customer
    WHERE customer_id = 1
);

-- Exercise 2: students table

-- >>> Update

/*
1. ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates.
Update both their birth_dates to 02/11/1998.
*/
UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name IN ('Lea', 'Marc') 
AND last_name= 'Benichou';

-- 2. Change the last_name of David from ‘Grez’ to ‘Guez’
UPDATE students
SET last_name = 'Guez'
WHERE first_name='David' AND last_name='Grez';

-- >>> Delete
-- 1. Delete the student named ‘Lea Benichou’ from the table
DELETE FROM students WHERE first_name='Lea' AND last_name='Benichou';

-- >>> Count
-- 1. Count how many students are in the table.
SELECT COUNT(*) FROM students;

-- 2. Count how many students were born after 1/01/2000.
SELECT COUNT(*) FROM students WHERE birth_date > '2000-01-01';

-- >>> Insert / Alter
-- 1. Add a column to the student table called math_grade.
ALTER TABLE students
ADD COLUMN math_grade SMALLINT

-- 2. Add 80 to the student which id is 1.
UPDATE students
SET math_grade = 80
WHERE id = 1;

-- 3. Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade = 90
WHERE id IN (2, 4);

-- 4. Add 40 to the student which id is 6
UPDATE students
SET math_grade = 40
WHERE id = 6;

-- 5. Count how many students have a grade bigger than 83
SELECT COUNT(*) FROM students WHERE math_grade > 83;

-- 6. Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students(id, first_name, last_name, birth_date, math_grade)
VALUES (8,
        'Omer',
        'Simpson',
        (SELECT birth_date FROM students WHERE first_name='Omer' AND last_name='Simpson'),
        70
        );

/*
7. Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although 
he received 2 different grades because he retook the math exam.
Bonus: Count how many grades each student has.
*/

SELECT first_name, last_name, COUNT(math_grade) AS number_of_grades
FROM students
GROUP BY first_name, last_name;

-- >>> SUM
-- 1. Find the sum of all the students grades.
SELECT SUM(math_grade) FROM students;

-- Exercise 3 : Items and customers

/*
Part I :
1. Create a table named purchases. It should have 3 columns :customer_id, item_id, quantity_purchased
*/
CREATE TABLE purchases(
    id SERIAL PRIMARY KEY,
    customers_id INTEGER,
    item_id INTEGER,
    quantity_purchased SMALLINT NOT NULL,
    FOREIGN KEY (customers_id) REFERENCES customers(customers_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

-- 2. Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bougth two small desks
INSERT INTO purchases(id, customers_id, item_id, quantity_purchased) 
VALUES (1, 3, 3, 1),
       (2, 5, 2, 10),
       (3, 1, 1, 2);


/* 
Part II
1. Use SQL to get the following from the database:
*/
-- 1.1. All purchases. Is this information useful to us?
-- >>> Answer : This raw information is not very useful on its own, we need to make it meaningful
SELECT * FROM purchases;

-- 1.2. All purchases, joining with the customers table.
SELECT p.id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.quantity_purchased
FROM purchases AS p
INNER JOIN customers AS c
ON  p.customers_id = c.customers_id

-- 1.3. Purchases of the customer with the ID equal to 5.
SELECT p.id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.quantity_purchased
FROM purchases AS p
INNER JOIN customers AS c
ON  p.customers_id = c.customers_id
WHERE p.customers_id = 5;

-- 1.4. Purchases for a large desk AND a small desk
SELECT p.id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.quantity_purchased
FROM purchases AS p
INNER JOIN customers AS c
ON  p.customers_id = c.customers_id
WHERE item_id IN (1, 2);

-- 2. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name, last name and Item name
SELECT
       c.first_name,
       c.last_name,
       i.item_name,
       p.quantity_purchased
FROM purchases AS p
INNER JOIN customers AS c ON  p.customers_id = c.customers_id
INNER JOIN items AS i ON p.item_id = i.item_id

-- 3. Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). 
-- Does this work? Why/why not?
/*
>>> ANSWER : A NULL value, by definition, means "no value."
It doesn't reference any specific record in the items table,
so it does not violate the foreign key's rule of referential integrity.
*/
INSERT INTO purchases (id, customers_id, quantity_purchased)
VALUES (4, 2, 5);