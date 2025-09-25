-- Daily Challenge: Actors
-- In this exercise we will be using the actors table

CREATE TABLE actors(
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
    birth_date DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Matt', 'Damon', '08/10/1970', 5),
       ('George', 'Clooney', '06/05/1961', 2),
       ('Angelina', 'Jolie', '1975-06-04', 1),
       ('Jennifer', 'Aniston', '1969-02-11', 0);

-- Count how many actors are in the table
SELECT COUNT(*)
FROM actors

-- Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- Answer: We are getting errors because of the declaration in creating the table in which we put the condition NOT NULL
INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Abd el jabar', 'Lawzir');