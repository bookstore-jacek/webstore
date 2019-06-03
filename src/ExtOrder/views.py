from django.shortcuts import render
from django.views import View

from .models import ExtOrder as Order
from OrderedProduct.models import OrderedProduct
from Product.models import Product
from .forms import CustomerForm, CustomerRadioForm, ProductForm, ProductRadioForm
from Customer.models import Customer
from Product.models import Product
from SuppProd.models import SuppProd
from Supplier.models import Supplier

from functools import reduce
# Create your views here.
class Orders_add_view(View):
    template_name = "order/add_order.html"
    customers = []
    products = []
    customer_found = False
    customer_added = False
    choosen_cust = None
    choosen_prods = []
    product_found = False
    product_added = False

    def find_customers(self, some_data):
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

        self.customers = list(reduce(lambda x, y: x & y, customers))
    
    def find_products(self, some_data):
        text = some_data.strip().split(' ')
        products = []
        for n, word in enumerate(text):
            products.append(set())
            products[n].update([product for product in Product.objects.filter(name__icontains=word)])
        
        self.products = list(reduce(lambda x, y: x & y, products))

    def get(self, request, *args, **kwargs):
        customer_form = CustomerForm()
        product_form = ProductForm()

        context={
            "customer_form": customer_form,
            "cust_found": self.customer_found,
            "cust_added": self.customer_added,
            "choosen_cust": self.choosen_cust,
            "product_form": product_form,
            "choosen_prods": self.choosen_prods
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if 'first' in request.POST:
            customer_form = CustomerForm(request.POST)
            if customer_form.is_valid():
                self.customer_found = True
                self.find_customers(customer_form.cleaned_data.get('text'))
        else:
            customer_form = CustomerForm()
    
        if 'second' in request.POST:
            choosen_id = request.POST.get('choosen_customer')
            customer_radio_form = CustomerRadioForm([Customer.objects.get(id=choosen_id)], request.POST)
            if customer_radio_form.is_valid():
                self.customer_added = True
                self.choosen_cust = Customer.objects.get(id=choosen_id)
        else:
            customer_radio_form = CustomerRadioForm(self.customers)

        if 'third' in request.POST:
            product_form = ProductForm(request.POST)
            if product_form.is_valid():
                self.product_found = True
                self.customer_added = True
                self.customer_found = True
                self.find_products(product_form.cleaned_data.get('text'))
                print(self.product_found, self.customer_added, self.customer_found)
        else:
            product_form = ProductForm()
        
        if 'fourth' in request.POST:
            choosen_id = request.POST.get('choosen_product')
            product_radio_form = ProductRadioForm([Product.objects.get(id=choosen_id)], request.POST)
            if product_radio_form.is_valid():
                self.product_added = True
                self.choosen_prods += [Product.objects.get(id=choosen_id)]
                print(self.customer_added, self.customer_found)
        else:
            print(self.products)
            product_radio_form = ProductRadioForm(self.products)

        context={
            "customer_form": customer_form,
            "customer_radio_form": customer_radio_form,
            "cust_found": self.customer_found,
            "cust_added": self.customer_added,
            "choosen_cust": self.choosen_cust,
            "product_form": product_form,
            "product_radio_form": product_radio_form,
            "choosen_prods": self.choosen_prods
        }
        return render(request, self.template_name, context)


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