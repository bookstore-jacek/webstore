/* 
changed
    product_id -> id due to being the only id here
    paid -> enum to boolean, I cannot memorise why was it enum
*/

CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    quantity INT NULL,
    threshold INT NULL,
    supplier INT REFERENCES supplier
);