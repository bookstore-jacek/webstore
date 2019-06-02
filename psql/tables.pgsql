CREATE TYPE payment AS ENUM(
    'not_paid',
    'partly_paid',
    'fully_paid'
);

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

CREATE TABLE ext_order(
    id
        SERIAL
        PRIMARY KEY,
    customer_id
        INT
        REFERENCES customer,
    paid
        payment
        NOT NULL,
    submitted
        TIMESTAMP
        NOT NULL,
    finished
        TIMESTAMP,
    cancelled
        TIMESTAMP,
    CONSTRAINT cannot_be_finished_and_cancelled
        CHECK (finished IS NULL OR cancelled IS NULL)
);


CREATE TABLE product(
    id
        SERIAL
        PRIMARY KEY,
    name
        VARCHAR(50)
        NOT NULL,
    quantity
        INT
        DEFAULT 0,
    threshold
        INT
        DEFAULT 0,
    CONSTRAINT quantity_and_threshold_should_be_null_or_positive
        CHECK ((quantity IS NULL OR quantity >= 0)
          AND (threshold IS NULL OR threshold >= 0))
);

CREATE TABLE ordered_product(
    id 
        SERIAL
        PRIMARY KEY,
    order_id
        INT
        REFERENCES ext_order
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    product_id
        INT
        REFERENCES product
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    ordered
        TIMESTAMP,
    collected
        TIMESTAMP,
    finished
        TIMESTAMP,
    cancelled
        TIMESTAMP, 
    CONSTRAINT cannot_be_finished_and_cancelled
        CHECK (finished IS NULL OR cancelled IS NULL)
);

CREATE TABLE supp_prod(
    product_id
        INT
        REFERENCES product
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    supplier_id
        INT
        REFERENCES supplier
        ON UPDATE CASCADE
        ON DELETE CASCADE
);