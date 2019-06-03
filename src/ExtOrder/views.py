from django.shortcuts import render

# Create your views here.
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