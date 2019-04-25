CREATE ROLE worker WITH LOGIN PASSWORD 'ksiegarniaspoko';
GRANT SELECT, INSERT, UPDATE ON * TO worker;

CREATE ROLE extern WITH LOGIN PASSWORD 'asdflwdf';
GRANT SELECT ON product, ext_order, ordered_product TO extern;