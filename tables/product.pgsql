
CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    quantity INT NULL,
    threshold INT NULL,
    CONSTRAINT quantity_and_threshold_should_be_null_or_positive
    CHECK ((quantity IS NULL OR quantity >= 0) AND (threshold IS NULL OR threshold >= 0))
);