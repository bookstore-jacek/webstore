from django.shortcuts import render
from .models import Product
from .forms import ProductForm

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
#        )l


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



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'order_id': 1233434,
        }
        pdf = render_to_pdf('product/zamowienie.html', data)
        return HttpResponse(pdf, content_type='application/pdf')




#https://github.com/codingforentrepreneurs/Guides/blob/master/all/Render_to_PDF_in_Django.md