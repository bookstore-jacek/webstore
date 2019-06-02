CREATE ROLE worker WITH LOGIN PASSWORD 'ksiegarniaspoko';
GRANT SELECT, INSERT, UPDATE 
ON
    customer,
    ext_order,
    ordered_product,
    product,
    supp_prod,
    supplier 
TO worker;

CREATE ROLE extern WITH LOGIN PASSWORD 'asdflwdf';
GRANT SELECT ON product, ext_order, ordered_product TO extern;