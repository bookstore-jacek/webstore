
CREATE TABLE ordered_product(
    id 
        SERIAL
        PRIMARY KEY,
    order_id
        INT
        REFERENCES ext_order
        ON DELETE CASCADE,
    product_id
        INT
        REFERENCES product
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