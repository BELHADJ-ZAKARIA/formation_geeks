-- Exercise 1: DVD Rental

-- 1. Get a list of all the languages, from the language table.
SELECT * FROM language;

-- 2. Get a list of all films joined with their languages – select the following details : 
-- film title, description, and language name.
SELECT
    f.title,
    f.description,
    lan.name
from
    film AS f
INNER JOIN
    language AS lan ON f.language_id = lan.language_id;

-- 3. Get all languages, even if there are no films in those languages – select the following details : 
-- film title, description, and language name.
SELECT
    f.title,
    f.description,
    lan.name
from
    film AS f
RIGHT JOIN
    language AS lan ON f.language_id = lan.language_id;

-- 4. Create a new table called new_film with the following columns :
-- id, name. Add some new films to the table.
CREATE TABLE new_film(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL
);

INSERT INTO new_film(name) VALUES
('Dune: Part Two'),
('Furiosa: A Mad Max Saga'),
('The Zone of Interest'),
('Poor Things');

/*
5. Create a new table called customer_review, which will contain film reviews that customers will make.
Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
It should have the following columns:
-- review_id – film_id – language_id – title – score – review_text – last_update.
*/
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER,
    language_id INTEGER,
    title VARCHAR(100) NOT NULL,
    score SMALLINT NOT NULL,
    review_text TEXT,
    last_update DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id)
);
SELECT*from language
-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES (
    (SELECT id FROM new_film WHERE name = 'Dune: Part Two'),
    (SELECT language_id FROM language WHERE name = 'English'),
    'A masterclass in sci-fi filmmaking',
    10,
    'The visuals, the sound design, the acting... everything was perfect. A truly epic cinematic experience.'
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES (
    (SELECT id FROM new_film WHERE name = 'Furiosa: A Mad Max Saga'),
    (SELECT language_id FROM language WHERE name = 'English'),
    'A breathtaking prequel',
    9,
    'A relentless and visually stunning action film that successfully expands the Mad Max universe.'
);

-- 7. Delete a film that has a review from the new_film table,
-- what happens to the customer_review table?
-- >>> ANSWER : We deleted automatically all row has link new_film id =2 because of this (ON DELETE CASCADE)
DELETE FROM new_film WHERE id = 2;

-- Exercise 2 : DVD Rental
-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.

UPDATE film -- i change the languge of first two row into 
SET language_id = 2
WHERE film_id IN (1, 2)

-- 2. Which foreign keys (references) are defined for the customer table?
-- How does this affect the way in which we INSERT into the customer table?

/* 
-- >>> ANSWER:
The customer table has foreign keys that reference the address table. Specifically, the address_id in the customer table is a foreign key that references the address_id in the address table.
This foreign key constraint means that every new record you INSERT into the customer table must have a valid address_id that already exists in the address table.
*/

-- 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- >>> ANSWER: Not easy step because we have foreign key constraint, the deleting can affect other table 

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title
FROM rental
INNER JOIN payment ON rental.rental_id = payment.rental_id
INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id 
INNER JOIN film ON film.film_id = inventory.film_id
WHERE return_date IS NULL
ORDER BY payment.amount DESC
LIMIT 30

/*
6. Your friend is at the store, and decides to rent a movie.
He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
*/

-- 6.1. The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT
    title
FROM
    film AS f
INNER JOIN film_actor AS fa ON f.film_id = fa.film_id
INNER JOIN actor AS a ON fa.actor_id = a.actor_id
WHERE
    f.description LIKE '%Sumo Wrestler%'
    AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- 6.2. The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT
    title
FROM
    film
WHERE
    length < 60
    AND rating = 'R'
    AND description LIKE '%Documentary%';

-- 6.3. The 3rd film : A film that his friend Matthew Mahan rented.
-- He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT
    f.title
FROM
    film AS f
INNER JOIN
    inventory AS i ON f.film_id = i.film_id
INNER JOIN
    rental AS r ON i.inventory_id = r.inventory_id
INNER JOIN
    payment AS p ON r.rental_id = p.rental_id
INNER JOIN
    customer AS c ON r.customer_id = c.customer_id
WHERE
    c.first_name = 'Matthew' AND c.last_name = 'Mahan'
    AND p.amount > 4.00
    AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 6.4. The 4th film : His friend Matthew Mahan watched this film, as well.
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT
    f.title
FROM
    film AS f
INNER JOIN
    inventory AS i ON f.film_id = i.film_id
INNER JOIN
    rental AS r ON i.inventory_id = r.inventory_id
INNER JOIN
    customer AS c ON r.customer_id = c.customer_id
WHERE
    c.first_name = 'Matthew' AND c.last_name = 'Mahan'
    AND (f.title LIKE '%Boat%' OR f.description LIKE '%boat%')
ORDER BY
    f.replacement_cost DESC
LIMIT 1;
