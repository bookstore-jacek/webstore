from django.shortcuts import render
from django.views import View

from .models import ExtOrder as Order
from OrderedProduct.models import OrderedProduct
from Product.models import Product
# Create your views here.

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

def add_order_view(request, *args, **kwargs):
    return render(request, "order/add_order.html", {})

def check_status_view(request, *args, **kwargs):
    return render(request, "order/check_status.html", {})