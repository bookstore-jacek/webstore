from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from ExtOrder.models import ExtOrder as Order

# Create your views here.
def customers_view(request, *args, **kwargs):
    customers = list(Customer.objects.all())
    def sort_id(val):
        return val.id
    customers.sort(key=sort_id)

    all_orders_per_cust = [Order.objects.filter(customer_id=cust.id).count() for cust in customers]
    pending_orders_per_cust = [
        Order.objects.filter(customer_id=cust.id, finished__isnull=True, cancelled__isnull=True).count()
            for cust in customers
        ]
    
    context = {
        'customers': zip(
            customers,
            all_orders_per_cust,
            pending_orders_per_cust
        )
    }
    return render(request, "customer/customers.html", context)

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