from django.shortcuts import render

# Create your views here.
def add_product_view(request, *args, **kwargs):
    return render(request, "product/add_product.html", {})

def bulk_order_view(request, *args, **kwargs):
    return render(request, "product/bulk_order.html", {})

def find_book_view(request, *args, **kwargs):
    return render(request, "product/find_book.html", {})