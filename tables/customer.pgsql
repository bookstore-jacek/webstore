/* 
renamed
    customer_id -> id as it is the only id here

changed
    phone -> changed type to CHAR as it doesn't vary in length
    email -> extended capacity
    password -> passhash as it will be hashed
                also changed to TEXT as we have to add some 'soap' string to extend it before hashing
*/

CREATE TABLE customer(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    phone CHAR(13) UNIQUE NOT NULL,
    email VARCHAR(30) UNIQUE NULL,
    passhash TEXT NULL
);