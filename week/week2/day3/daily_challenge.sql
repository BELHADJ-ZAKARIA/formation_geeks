-- Part I: One-to-One Relationship

-- 1. Create Customer Table / Profile Table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);


CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INTEGER UNIQUE,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES Customer(id)
        ON DELETE CASCADE
);

-- 2. Insert Customers
INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- 3. Insert Customer Profiles using Subqueries
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (
    TRUE,
    (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')
);

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (
    FALSE,
    (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);


-- Display the first_name of the LoggedIn customers
SELECT
    C.first_name
FROM
    Customer C
INNER JOIN
    CustomerProfile CP ON C.id = CP.customer_id
WHERE
    CP.isLoggedIn = TRUE;

-- Display the number of customers that are not LoggedIn
SELECT
    COUNT(C.id) AS NotLoggedInCustomerCount
FROM
    Customer C
LEFT JOIN
    CustomerProfile CP ON C.id = CP.customer_id
WHERE
    CP.isLoggedIn = FALSE OR CP.isLoggedIn IS NULL;

-- Part II: Many-to-Many Relationship (Book, Student, Library)

-- 1. Create Book Table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- 2. Insert Books
INSERT INTO Book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- 3. Create Student Table
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INTEGER,
    CONSTRAINT age_max_15 CHECK (age <= 15)
);

-- 4. Insert Students
INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- 5. Create Library (Junction) Table
CREATE TABLE Library (
    book_fk_id INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    CONSTRAINT fk_book
        FOREIGN KEY (book_fk_id)
        REFERENCES Book(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_student
        FOREIGN KEY (student_fk_id)
        REFERENCES Student(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 6. Add 4 records in the junction table, using subqueries
INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date) VALUES (
    (SELECT student_id FROM Student WHERE name = 'John'),
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    '2022-02-15'
);

INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date) VALUES (
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    '2021-03-03'
);

INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date) VALUES (
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    '2021-05-23'
);

INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date) VALUES (
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    '2021-08-12'
);

-- 7. Display the data

-- Select all the columns from the junction table
SELECT * FROM Library;

-- Select the name of the student and the title of the borrowed books
SELECT
    S.name AS student_name,
    B.title AS book_title,
    L.borrowed_date
FROM
    Library L
JOIN
    Student S ON L.student_fk_id = S.student_id
JOIN
    Book B ON L.book_fk_id = B.book_id
ORDER BY
    S.name, L.borrowed_date;

-- Select the average age of the children that borrowed the book
SELECT
    ROUND(AVG(S.age), 2) AS average_age_for_alice
FROM
    Library L
JOIN
    Student S ON L.student_fk_id = S.student_id
JOIN
    Book B ON L.book_fk_id = B.book_id
WHERE
    B.title = 'Alice In Wonderland';

-- Delete a student from the Student table
DELETE FROM Student WHERE name = 'John';

-- what happened in the junction table ?
-- ANSWER: When 'John' was deleted from Student, his corresponding record
-- in the Library table was automatically deleted due to the ON DELETE CASCADE constraint.