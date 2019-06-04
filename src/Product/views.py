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

# Create your views here.
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


def html_to_pdf_view(request):
       
    ord_prods = OrderedProduct.objects.filter(ordered__isnull=True)
    products = [Product.objects.get(id=x.product_id) for x in ord_prods]

    # bulk_ord = Product.objects.filter(ordered__isnull=True)
    # products = [Product.objects.get(id=x.product_id) for x in ord_prods]

    html_string = render_to_string('product/zamowienie.html', {
        'actual_date_time': now.strftime("%d.%m.%Y %H:%M"),
        'products': products,
        })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/zamowienie.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('zamowienie.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="zamowienie.pdf"'
        return response

    return response