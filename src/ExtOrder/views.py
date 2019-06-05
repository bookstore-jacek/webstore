from django.shortcuts import render
from django.views import View
from django.db.models.functions import Now

from .models import ExtOrder as Order
from .forms import OrderForm, OrderSearchForm
from .utils import find_orders, attach_products, sort_id, filter_orders

from Product.models import Product
from Customer.models import Customer
from OrderedProduct.models import OrderedProduct
# Create your views here.

def find_order_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = OrderSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('user_input')
            orders = find_orders(data)
            orders = filter_orders(orders, form.cleaned_data.get('status'))
            form = OrderSearchForm()
        else:
            orders = list(Order.objects.all())
    else:
        form = OrderSearchForm()
        orders = list(Order.objects.all())
    print(orders)

    context={
        "form": form,
        "orders": attach_products(orders)
    }
    return render(request, "order/find_order.html", context)


def add_order_view(request, *args, **kwargs):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            customer = data.get('phone'),
            products = [data.get(f'product{x}') for x in range(5) if data.get(f'product{x}') is not None]
            paid = data.get('paid')
            order = Order.objects.create(customer_id=customer[0].id, paid=paid, submitted=Now())
            for prod in products:
                ord_prod = OrderedProduct.objects.create(order_id=order.id, product_id=prod.id)
            form = OrderForm()
    else:
        form = OrderForm()

    context={
        "form": form
    }
    return render(request, "order/add_order.html", context)

def all_orders_view(request, *args, **kwargs):
    orders = list(Order.objects.all())
    orders.sort(key=sort_id)
    ord_products = [OrderedProduct.objects.filter(order_id=order.id) for order in orders]
    products = []
    for ord_prod_filtered in ord_products:
        products.append([Product.objects.get(id=ord_prod.product_id) for ord_prod in ord_prod_filtered])

    context = {
        'orders': zip(orders, products)
    }
    return render(request, "order/all_orders.html", context)

def pending_orders_view(request, *args, **kwargs):
    not_finished_orders = set(Order.objects.filter(finished__isnull=True))
    not_cancelled_orders = set(Order.objects.filter(cancelled__isnull=True))
    orders = list(not_cancelled_orders & not_finished_orders)
    orders.sort(key=sort_id)
    ord_products = [OrderedProduct.objects.filter(order_id=order.id) for order in orders]
    products = []
    for ord_prod_filtered in ord_products:
        products.append([Product.objects.get(id=ord_prod.product_id) for ord_prod in ord_prod_filtered])

    context = {
        'orders': zip(orders, products)
    }
    return render(request, "order/pending_orders.html", context)



def check_status_view(request, *args, **kwargs):
    return render(request, "order/check_status.html", {})