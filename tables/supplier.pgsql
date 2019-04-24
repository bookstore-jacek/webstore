
CREATE TABLE supplier(
    id
        SERIAL
        PRIMARY KEY,
    name
        VARCHAR(30)
        UNIQUE
        NOT NULL,
    website
        VARCHAR(30)
        UNIQUE
);