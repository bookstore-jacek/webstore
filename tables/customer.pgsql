/* 
renamed
    customer_id -> id as it is the only id here

changed
    phone -> changed type to char as it doesn't vary in length
    email -> extended capacity
    password -> passhash as it will be hashed
                also changed to text as we have to add some 'soap' string to extend it before hashing
*/

CREATE TABLE customer(
    id SERIAL PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    phone char(13) UNIQUE NOT NULL,
    email varchar(30) UNIQUE NULL,
    passhash text NULL
);