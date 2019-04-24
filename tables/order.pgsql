
CREATE TABLE ext_order(
    id
        SERIAL
        PRIMARY KEY,
    paid
        BOOLEAN
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