from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models.functions import Now

from .models import ExtOrder as Order
from .forms import OrderForm, OrderSearchForm, EditForm, FindForm
from .utils import find_orders, attach_products, sort_id, filter_orders

from Product.models import Product
from Customer.models import Customer
from OrderedProduct.models import OrderedProduct

from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

import base64
import binascii
from io import BytesIO
# Create your views here.

def find_order_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = OrderSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('user_input')
            orders = find_orders(data)
            orders.sort(key=sort_id)
            orders = filter_orders(orders, form.cleaned_data.get('status'))
            form = OrderSearchForm()
        else:
            orders = list(Order.objects.all())
    else:
        form = OrderSearchForm()
        orders = list(Order.objects.all())

    orders.sort(key=sort_id)

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
                ord_prod = OrderedProduct.objects.create(
                    order_id=order.id,
                    product_id=prod.id,
                    ordered=Now()
                )
            form = OrderForm()
    else:
        form = OrderForm()

    context={
        "form": form
    }
    return render(request, "order/add_order.html", context)

def detail_view(request, id):
    obj = get_object_or_404(Order, id=id)
    order, products = list(attach_products([obj]))[0]
    ord_prods = list(OrderedProduct.objects.filter(order_id=obj.id))
    products.sort(key=sort_id)
    ord_prods.sort(key=sort_id)

    if request.method == 'POST':
        form = EditForm(request.POST)
        print(1)
        if form.is_valid():
            paid = form.cleaned_data.get('paid')
            status = form.cleaned_data.get('status')
            if status == 'cancelled' and order.cancelled is None and order.finished is None:
                order.cancelled = Now()
                order.paid = paid
                order.save()
                for prod in ord_prods:
                    prod.cancelled = Now()
                    prod.save()
            elif status == 'finished' and order.cancelled is None and order.finished is None:
                order.finished = Now()
                order.paid = paid
                order.save()
                for prod in ord_prods:
                    prod.finished = Now()
                    prod.save()
            form = EditForm()
    else:
        form = EditForm()

    context = {
        'order': order,
        'products': zip(products, ord_prods),
        "form": form
    }
    return render(request, "order/order_details.html", context)

def check_status_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data.get('ord_id')
            order, products = list(attach_products([order]))[0]
            form = FindForm()
        else:
            order = ''
            products = ''
    else:
        form = FindForm()
        order = ''
        products = ''
    context = {
        'form': form,
        'order': order,
        'products': products
    }
    return render(request, "order/check_status.html", context)
