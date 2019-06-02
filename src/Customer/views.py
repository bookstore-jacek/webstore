from django.shortcuts import render

# Create your views here.
def customers_view(request, *args, **kwargs):
    return render(request, "customers.html", {})