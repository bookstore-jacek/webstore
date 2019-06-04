-- CUSTOMERS
INSERT INTO customer (first_name,last_name,phone,email,passhash)
    VALUES ('Adam','Kowalski',123456789,'adamk@wp.pl','qwertyui');
INSERT INTO customer (first_name,last_name,phone,email,passhash)
    VALUES ('Krystian','Wolski',556677889,'kryst@wp.pl','jlllakkk12');
INSERT INTO customer (first_name,last_name,phone)
    VALUES ('Tomasz','Leński',789678567);
INSERT INTO customer (first_name,last_name,phone)
    VALUES ('Karol','Polański',456567765);

-- PRODUCTS
INSERT INTO product (name,quantity,threshold)
    VALUES ('Potop',3,1);

INSERT INTO product (name,quantity)
    VALUES ('Przepisy na każdy dzień',2);

INSERT INTO product (name)
    VALUES ('Przewodnik po Karkonoszach');

INSERT INTO product (name,quantity,threshold)
    VALUES ('Kordian',1,1);

INSERT INTO product (name,quantity,threshold)
    VALUES ('Farby plakatowe 12 kolorów Astra',5,1);

-- ORDERS
INSERT INTO ext_order (customer_id, paid, submitted)
    VALUES (2, 'fully_paid', NOW());
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Potop'
        GROUP BY product.id;
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Kordian'
        GROUP BY product.id;

INSERT INTO ext_order (customer_id, paid, submitted)
    VALUES(1, 'not_paid', NOW());
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Przewodnik po Karkonoszach'
        GROUP BY product.id;
