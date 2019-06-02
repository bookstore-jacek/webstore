from django.shortcuts import render

# Create your views here.
def add_product_view(request, *args, **kwargs):
    return render(request, "add_product.html", {})

def bulk_order_view(request, *args, **kwargs):
    return render(request, "bulk_order.html", {})

def find_book_view(request, *args, **kwargs):
    return render(request, "find_book.html", {})