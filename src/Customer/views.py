from django.shortcuts import render

# Create your views here.
def customers_view(request, *args, **kwargs):
    return render(request, "customers.html", {})

def personal_orders_view(request, *args, **kwargs):
    return render(request, "personal_orders.html", {})

def account_view(request, *args, **kwargs):
    return render(request, "account.html", {})