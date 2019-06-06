from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def worker_view(request, *args, **kwargs):
    return render(request, "panel_home.html", {})
    
def add_customer_view(request, *args, **kwargs):
    return render(request, "add_customer.html", {})

def update_db_view(request, *args, **kwargs):
    return render(request, "update_db.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_us_view(request, *args, **kwargs):
    return render(request, "about_us.html", {})