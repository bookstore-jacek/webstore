from django.shortcuts import render
from ExtOrder.models import ExtOrder as Order
from OrderedProduct.models import OrderedProduct
from Product.models import Product
from Customer.forms import CustomerForm
from Customer.models import Customer

from .forms import ProductForm
from datetime import datetime
now = datetime.now()

from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML
from collections import Counter

# Create your views here.
def find_book_view(request, *args, **kwargs):
    return render(request, "product/find_book.html", {})


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
    ord_prods = OrderedProduct.objects.filter(ordered__isnull=True)
    products = [Product.objects.get(id=x.product_id) for x in ord_prods]

    # ilosc = [x.quantity - x.threshold for x in products]
    # ilosc = products.threshold - products.quantity

    # bulk_prod= Product.objects.all()
    
    products2 = [[str(prod.id) for prod in Product.objects.all() if prod.threshold != None and int(prod.threshold) - int(prod.quantity) > 0]]

    # instance_ids = [Product.objects.get(id=x.id) for x in bulk_ord] + [Product.objects.get(id=x.product_id) for x in ord_prods]
    # counter = Counter(instance_ids)

    external = Counter([str(x.product_id) for x in OrderedProduct.objects.filter(ordered__isnull=True)])
    internal = Counter([str(prod.id) for prod in Product.objects.all() if prod.threshold != None and prod.threshold != '0' and int(prod.threshold) - int(prod.quantity) > 0])
    all_keys = set({**external, **internal}.keys())
    order = []
    for i, key in enumerate(all_keys):
        value = 0
        if key in external.keys():
            value += external[key]
        if key in internal.keys():
            value += internal[key]
        order += [(Product.objects.get(id=int(key)), value)]

    internal_external_sum=Counter(internal+external)

    print(external)
    print(internal)
    print(internal_external_sum)
    print(order)

    html_string = render_to_string('product/zamowienie.html', {
        'actual_date_time': now.strftime("%d.%m.%Y %H:%M"),
        'prod': Product
        # 'ilosc_bulk' : products.quantity - products.threshold
        })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/zamowienie.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('zamowienie.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="zamowienie.pdf"'
        return response

    return response