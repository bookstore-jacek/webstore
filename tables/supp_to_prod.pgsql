
CREATE TABLE supp_prod(
    id
        SERIAL
        PRIMARY KEY,
    supplier
        INT
        REFERENCES supplier
        ON DELETE CASCADE,
    product
        INT
        REFERENCES product
        ON DELETE CASCADE
);