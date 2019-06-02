from django.shortcuts import render

# Create your views here.
from .forms import CustomerForm
from .models import Customer

def add_customer_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()

    context={
        "form":form
    }

    return render(request, "customer/add_customer.html",context)