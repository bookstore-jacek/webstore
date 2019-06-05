from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

from .models import Product

from functools import reduce

def sort_id(val):
        return val.id

def find_products(phrase):
    ret = []
    data = phrase.strip().split(' ')
    for word in data:
        ret.append(set(Product.objects.filter(name__icontains=word)))
    return list(reduce(lambda a, b: a & b, ret))