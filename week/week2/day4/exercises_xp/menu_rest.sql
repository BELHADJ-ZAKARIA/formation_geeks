-- Part I:
-- 1. Create Table Menu_Items
CREATE TABLE Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL UNIQUE, -- Unique constraint ensures item names are not duplicated
    item_price SMALLINT DEFAULT 0
);

