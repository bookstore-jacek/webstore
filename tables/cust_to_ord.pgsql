
CREATE TABLE cust_ord(
    id SERIAL
        PRIMARY
        KEY,
    customer
        INT
        NOT NULL
        REFERENCES customer
        ON DELETE CASCADE,
    ext_order
        INT
        NOT NULL
        UNIQUE
        REFERENCES ext_order
        ON DELETE CASCADE
);