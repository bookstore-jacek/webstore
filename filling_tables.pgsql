-- SUPPLIERS
INSERT INTO supplier (name,website)
    VALUES ('Tanie Książki','www.tanie-ksiazki.pl');
INSERT INTO supplier (name,website)
    VALUES ('Szybka Książka','www.szybkaksiazka.pl');
INSERT INTO supplier (name,website)
    VALUES ('Hurtownia książek','www.ksiazkianc.pl');

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
INSERT INTO supp_prod (supplier, product)
    SELECT supplier.id, MAX(product.id) FROM supplier, product
        WHERE supplier.name='Szybka Książka'
        GROUP BY supplier.id;

INSERT INTO product (name,quantity,threshold)
    VALUES ('Przepisy na każdy dzień',2,1);
INSERT INTO supp_prod (supplier, product)
    SELECT supplier.id, MAX(product.id) FROM supplier, product
        WHERE supplier.name='Tanie Książki'
        GROUP BY supplier.id;

INSERT INTO product (name,quantity,threshold)
    VALUES ('Przewodnik po Karkonoszach',1,1);
INSERT INTO supp_prod (supplier, product)
    SELECT supplier.id, MAX(product.id) FROM supplier, product
        WHERE supplier.name='Szybka Książka'
        GROUP BY supplier.id;

INSERT INTO product (name,quantity,threshold)
    VALUES ('Kordian',1,1);
INSERT INTO supp_prod (supplier, product)
    SELECT supplier.id, MAX(product.id) FROM supplier, product
        WHERE supplier.name='Tanie Książki'
        GROUP BY supplier.id;

INSERT INTO product (name,quantity,threshold)
    VALUES ('Farby plakatowe 12 kolorów Astra',5,1);
INSERT INTO supp_prod (supplier, product)
    SELECT supplier.id, MAX(product.id) FROM supplier, product
        WHERE supplier.name='Tanie Książki'
        GROUP BY supplier.id;

-- ORDERS
INSERT INTO ext_order (paid, submitted)
    VALUES ('1',to_timestamp('8 Apr 2019 13 34', 'DD Mon YYYY HH24 MI'));
INSERT INTO cust_ord (customer, ext_order)
    SELECT customer.id, MAX(ext_order.id) FROM customer, ext_order
        WHERE customer.phone='123456789'
        GROUP BY customer.id;
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Potop'
        GROUP BY product.id;
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Kordian'
        GROUP BY product.id;

INSERT INTO ext_order (paid, submitted)
    VALUES ('0',to_timestamp('10 Apr 2019 15 00', 'DD Mon YYYY HH24 MI'));
INSERT INTO cust_ord (customer, ext_order)
    SELECT customer.id, MAX(ext_order.id) FROM customer, ext_order
        WHERE customer.phone='789678567'
        GROUP BY customer.id;
INSERT INTO ordered_product (order_id, product_id)
    SELECT max(ext_order.id), product.id FROM product, ext_order 
        WHERE name='Przewodnik po Karkonoszach'
        GROUP BY product.id;


