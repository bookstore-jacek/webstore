from django.shortcuts import render
from django.views import View

from .models import ExtOrder as Order
from OrderedProduct.models import OrderedProduct
from Product.models import Product
from .forms import CustomerForm
from Customer.models import Customer

from functools import reduce
# Create your views here.

def find_customers(some_data):
    text = some_data.strip().split(' ')
    customers = []
    for n, word in enumerate(text):
        customers.append(set())
        try:
            num = int(word)
            customers[n].update([customer for customer in Customer.objects.filter(phone__contains=num)])
        except ValueError:
            pass
        customers[n].update([customer for customer in Customer.objects.filter(first_name__icontains=word)])
        customers[n].update([customer for customer in Customer.objects.filter(last_name__icontains=word)])
        customers[n].update([customer for customer in Customer.objects.filter(email__icontains=word)])
        for cust in customers[n]:
            print(n, cust)
    customers = list(reduce(lambda x, y: x & y, customers))
    return customers

def add_order_view(request):
    form = CustomerForm(request.POST or None)
    customers = []
    if form.is_valid():
        customers = find_customers(form.cleaned_data.get('text'))

    context={
        "form": form,
        "customers": customers
    }
    return render(request, "order/add_order.html", context)

class Orders_list_view(View):
    template_name = "order/all_orders.html"
    orders = Order.objects.all()
    ord_products = [OrderedProduct.objects.filter(order_id=order.id) for order in orders]
    products = []
    for ord_prod_filtered in ord_products:
        products.append([Product.objects.get(id=ord_prod.product_id) for ord_prod in ord_prod_filtered])

    def get_queryset(self):
        return zip(self.orders, self.products)
    
    def get(self, request, *args, **kwargs):
        context = {
            'orders': self.get_queryset()
        }
        return render(request, self.template_name, context)

def find_order_view(request, *args, **kwargs):
    return render(request, "order/find_order.html", {})

def all_orders_view(request, *args, **kwargs):
    return render(request, "order/all_orders.html", {})

def pending_orders_view(request, *args, **kwargs):
    return render(request, "order/pending_orders.html", {})

def check_status_view(request, *args, **kwargs):
    return render(request, "order/check_status.html", {})