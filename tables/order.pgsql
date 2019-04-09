/* 
removed
    ordered -> as it is storred separately for each product

changed
    paid -> enum to boolean, I cannot memorise why was it enum
    all columns with xxxx_id syntax -> renamed to just name of reffered column and order_id to id for simplicity
*/

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    products INT[], -- array cannot explicitly contain foreign keys
    customer INT REFERENCES customer ON DELETE RESTRICT,
    paid BOOLEAN NOT NULL,
    submitted TIMESTAMP NOT NULL,
    finished TIMESTAMP NULL,
    cancelled TIMESTAMP NULL,
    CHECK cannot_be_finished_and_cancelled (finished IS NULL OR cancelled IS NULL)
);