from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def customers_view(request, *args, **kwargs):
    return render(request, "customer/customers.html", {})

def personal_orders_view(request, *args, **kwargs):
    return render(request, "customer/personal_orders.html", {})

def account_view(request, *args, **kwargs):
    return render(request, "customer/account.html", {})

def add_customer_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CustomerForm()   
    context={
        "form": form
    }
    return render(request, "customer/add_customer.html", context)

def add_product_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CustomerForm()   
    context={
        "form": form
    }
    return render(request, "product/add_product.html", context)
