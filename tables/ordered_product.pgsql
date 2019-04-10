
CREATE TABLE ordered_product(
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES ext_order ON DELETE CASCADE,
    product_id INT REFERENCES product ON DELETE CASCADE,
    ordered TIMESTAMP NULL,
    collected TIMESTAMP NULL,
    finished TIMESTAMP NULL,
    cancelled TIMESTAMP NULL, 
    CONSTRAINT cannot_be_finished_and_cancelled CHECK (finished IS NULL OR cancelled IS NULL)
);