from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def bulk_order_view(request, *args, **kwargs):
    return render(request, "product/bulk_order.html", {})

def find_book_view(request, *args, **kwargs):
    return render(request, "product/find_book.html", {})


def add_product_view(request):
    form = ProductForm(request.POST or None)
    #form.clean_customer()
    if form.is_valid():
        form.save()
        form=ProductForm()
   
    context={
        "form": form
    }
    return render(request, "product/add_product.html", context)