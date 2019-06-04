from django.shortcuts import render
from django.views import View
from django.db.models.functions import Now

from .models import ExtOrder as Order
from .forms import OrderForm
from Product.models import Product
from Customer.models import Customer
from OrderedProduct.models import OrderedProduct
# Create your views here.

def order_add_view(request, *args, **kwargs):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            customer = data.get('phone'),
            products = [data.get(f'product{x}') for x in range(5) if data.get(f'product{x}') is not None]
            paid = data.get('paid')
            order = Order.objects.create(customer_id=customer.id, paid=paid, submitted=Now())
            for prod in products:
                OrderedProduct.objects.create(order_id=order.id, product_id=prod.id)
            form = OrderForm()
    else:
        form = OrderForm()

    context={
        "form": form
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