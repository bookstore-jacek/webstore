from django.shortcuts import render
from .forms import CustomerForm, CustomerSearchForm
from .models import Customer
from .utils import find_customers, sort_id
from ExtOrder.models import ExtOrder as Order

# Create your views here.
def customers_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CustomerSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('user_input')
            customers = find_customers(data)
            form = CustomerSearchForm()
        else:
            customers = list(Customer.objects.all())
    else:
        form = CustomerSearchForm()
        customers = list(Customer.objects.all())

    customers.sort(key=sort_id)
    all_orders_per_cust = [Order.objects.filter(customer_id=cust.id).count() for cust in customers]
    pending_orders_per_cust = [
        Order.objects.filter(customer_id=cust.id, finished__isnull=True, cancelled__isnull=True).count()
            for cust in customers
    ]
    
    context = {
        "form" : form,
        'customers': zip(
            customers,
            all_orders_per_cust,
            pending_orders_per_cust
        )
    }
    return render(request, "customer/customers.html", context)

def personal_orders_view(request, *args, **kwargs):
    return render(request, "customer/personal_orders.html", {})

def add_customer_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CustomerForm()
    context={
        "form": form
    }
    return render(request, "customer/add_customer.html", context)