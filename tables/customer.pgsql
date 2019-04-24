
CREATE TABLE customer(
    id
        SERIAL
        PRIMARY KEY,
    first_name
        VARCHAR(20)
        NOT NULL,
    last_name
        VARCHAR(20)
        NOT NULL,
    phone
        CHAR(13)
        UNIQUE
        NOT NULL,
    email
        VARCHAR(30)
        UNIQUE,
    passhash
        TEXT
);