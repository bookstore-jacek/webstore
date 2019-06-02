from django.shortcuts import render

# Create your views here.
def find_order_view(request, *args, **kwargs):
    return render(request, "find_order.html", {})

def all_orders_view(request, *args, **kwargs):
    return render(request, "all_orders.html", {})

def pending_orders_view(request, *args, **kwargs):
    return render(request, "pending_orders.html", {})

def add_order_view(request, *args, **kwargs):
    return render(request, "add_order.html", {})