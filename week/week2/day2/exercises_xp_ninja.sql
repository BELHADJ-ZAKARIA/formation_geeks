-- Exercise 1 : Bonus Public Database (Continuation of XP)
-- 1. Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT p.id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.quantity_purchased
FROM purchases AS p
INNER JOIN customers AS c
ON  p.customers_id = c.customers_id
ORDER BY 
    c.first_name DESC,
    c.last_name DESC
LIMIT 2;

-- 2. Use SQL to delete all purchases made by Scott.
DELETE FROM purchases
WHERE customers_id IN (
    SELECT customers_id
    FROM customers
    WHERE first_name = 'Scott' AND last_name = 'Scott'
);

-- 3. Does Scott still exist in the customers table, 
-- even though he has been deleted? Try and find him.
SELECT * FROM customers
WHERE first_name = 'Scott' AND last_name = 'Scott';

/*
4. Use SQL to find all purchases. Join purchases with the customers table,
so that Scott’s order will appear, although instead of the customer’s first and last name,
you should only see empty/blank. (Which kind of join should you use?).
*/ 
-- >>> ANSWER: LEFT JOIN

-- READ THIS!!!>>> Scott's purchases have already been deleted from the purchases table.
-- Therefore, it's impossible to "find" and display his orders. 
-- he type of join you are describing—one that shows all records 
-- from one table and leaves the other table's fields blank if there's no match—is a LEFT JOIN
SELECT * FROM purchases;
SELECT
    c.first_name,
    c.last_name,
    p.quantity_purchased
FROM
    purchases AS p
LEFT JOIN
    customers AS c ON p.customers_id = c.customers_id;

/*
Use SQL to find all purchases. Join purchases with the customers table,
so that Scott’s order will NOT appear. (Which kind of join should you use?)
*/
-- >>> ANSWER: RIGHT JOIN
SELECT
    c.first_name,
    c.last_name,
    p.quantity_purchased
FROM
    purchases AS p
RIGHT JOIN
    customers AS c ON p.customers_id = c.customers_id;