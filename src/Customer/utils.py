from .models import Customer
from functools import reduce

def sort_id(val):
        return val.id

def find_customers(phrase):
    ret = []
    data = phrase.strip().split(' ')
    for n, word in enumerate(data):
        ret.append(set())
        try:
            int(word)
            ret[n].update(list(Customer.objects.filter(phone__contains=word)))
        except ValueError:
            pass
        ret[n].update(list(Customer.objects.filter(first_name__icontains=word)))
        ret[n].update(list(Customer.objects.filter(last_name__icontains=word)))
        ret[n].update(list(Customer.objects.filter(email__icontains=word)))
    return list(reduce(lambda a, b: a & b, ret))