from .models import ExtOrder as Order
from Product.models import Product
from Customer.models import Customer
from Customer.utils import find_customers
from OrderedProduct.models import OrderedProduct

def sort_id(val):
    return val.id

def find_orders(phrase):
    ret = []
    data = phrase.strip().split(' ')
    return list(reduce(lambda a, b: a & b, ret))

def filter_orders(orders, status):
    pass

def attach_products(orders):
    pass