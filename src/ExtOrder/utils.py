from .models import ExtOrder as Order
from Product.models import Product
from Product.utils import find_products
from Customer.models import Customer
from Customer.utils import find_customers
from OrderedProduct.models import OrderedProduct

def sort_id(val):
    return val.id

def find_orders(phrase):
    products = find_products(phrase)
    customers = find_customers(phrase)
    ord_products_lists = [
        OrderedProduct.objects.filter(product_id=prod.id)
            for prod in products
    ]
    orders = set()
    for ord_products in ord_products_lists:
        orders.update([
            Order.objects.get(id=ord_prod.order_id)
                for ord_prod in ord_products
        ])
    for cust in customers:
        orders.update(list(Order.objects.filter(customer_id=cust.id)))
    return list(orders)

def filter_orders(orders, status):
    if status == 'unfinished':
        return list(filter(lambda x: x.finished is None and x.cancelled is None, orders))
    if status == 'finished':
        return list(filter(lambda x: x.finished is not None, orders))
    if status == 'cancelled':
        return list(filter(lambda x: x.cancelled is not None, orders))
    return orders
   
def attach_products(orders):
    ord_products = [OrderedProduct.objects.filter(order_id=order.id) for order in orders]
    products = []
    for ord_prod_filtered in ord_products:
        products.append([
            Product.objects.get(id=ord_prod.product_id)
                for ord_prod in ord_prod_filtered
        ])
    return zip(orders, products)