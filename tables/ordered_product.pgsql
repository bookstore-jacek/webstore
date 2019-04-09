/* 
removed
    New -> it is always the same date as submitted in order

changed
    order_product_id -> renamed to be shorter and extracted 2 foreign keys from it
    supplier_name -> changed to int due to change in supplier table
*/

CREATE TABLE ordered_product(
    ord_prod_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES ext_order ON DELETE CASCADE,
    product_id INT REFERENCES product ON DELETE CASCADE,
    ordered TIMESTAMP NULL,
    collected TIMESTAMP NULL,
    finished TIMESTAMP NULL,
    cancelled TIMESTAMP NULL, 
    CONSTRAINT cannot_be_finished_and_cancelled CHECK (finished IS NULL OR cancelled IS NULL)
);