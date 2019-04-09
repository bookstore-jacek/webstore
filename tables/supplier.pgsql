/* 
changed
    supplier_name -> extracted an id from it for auto incrementation
    name -> extended length just in case
*/

CREATE TABLE supplier(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    website VARCHAR(30) UNIQUE NULL
);