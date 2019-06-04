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

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf #created in step 4

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



# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


# def myview(request):
#     #Retrieve data or whatever you need
#     return render_to_pdf(
#             '/templates/product/zamowienie.html',
#             {
#                 'pagesize':'A4',
#                 'mylist': results,
#             }
 #       )


#def bulk_order_view(request, *args, **kwargs):
#    return render(request, "product/bulk_order.html", {}#)#


#    return render_to_pdf(
#            'zamowienie.html',
#            {
#                'pagesize':'A4',
#            }
#        )


# class GeneratePdf_view(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = PDF_generator('/product/zamowienie.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')



# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'title': "zażółć gęślą jaźń:",
#             'actual_date': now.strftime("%d.%m.%Y %H:%M"),
#         }
#         pdf = render_to_pdf('product/zamowienie.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

# from django.http import HttpResponse
# from django.views.generic import View

# from .utils import render_to_pdf #created in step 4

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         produkty = Product.objects.all()      
#         # data = {'produkty': produkty}
#         pdf = render_to_pdf('product/zamowienie.html', {'produkty': produkty})
#         return HttpResponse(pdf, content_type='application/pdf')



from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
        
    ord_prods = OrderedProduct.objects.filter(ordered__in=(""))
    products = [Product.objects.get(id=x.product_id) for x in ord_prods]
    print len (products)
    html_string = render_to_string('product/zamowienie.html', {
        'paragraphs': paragraphs,
        'actual_date_time': now.strftime("%d.%m.%Y %H:%M"),
        'products': products,
        'Product': Product,
        'ord_prods': ord_prods
        
        })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/zamowienie.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('zamowienie.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="zamowienie.pdf"'
        return response

    return response