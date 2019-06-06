from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string


from ExtOrder.models import ExtOrder as Order
from OrderedProduct.models import OrderedProduct
from Product.models import Product
from .forms import ProductForm, ProductSearchForm
from .utils import sort_id, find_products

from weasyprint import HTML, CSS
from collections import Counter
import datetime



# Create your views here.
def staff_find_book_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('user_input')
            products = find_products(data)
            form = ProductSearchForm()
        else:
            products = list(Product.objects.all())
    else:
        form = ProductSearchForm()
        products = list(Product.objects.all())

    context = {
        'form' : form,
        'products': products
    }
    return render(request, "product/staff_find_book.html", context)

def find_book_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('user_input')
            products = find_products(data)
            form = ProductSearchForm()
        else:
            products = list(Product.objects.all())
    else:
        form = ProductSearchForm()
        products = list(Product.objects.all())

    context = {
        'form' : form,
        'products': products
    }
    return render(request, "product/find_book.html", context)


def add_product_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
   
    context={
        "form": form,
    }
    return render(request, "product/add_product.html", context)


def html_to_pdf_view(request):
    now = datetime.datetime.now()
    external = Counter([str(x.product_id) for x in OrderedProduct.objects.filter(ordered__isnull=True)])
    internal = {str(prod.id): prod.threshold-prod.quantity for prod in Product.objects.all() if prod.threshold - prod.quantity > 0}
    all_keys = set({**external, **internal}.keys())
    order = []
    for i, key in enumerate(all_keys):
        value = 0
        if key in external.keys():
            value += external[key]
        if key in internal.keys():
            value += internal[key]
        order += [(Product.objects.get(id=int(key)), value)]

    html_string = render_to_string('product/bulk_order.html', {
        'actual_date_time': now.strftime("%d.%m.%Y %H:%M"),
        'order': order
    })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/zamowienie.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('zamowienie.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="zamowienie.pdf"'
        return response

    return response


def edit_view(request,id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'product': obj,
    }

    return render(request, "product/product_edit.html", context)