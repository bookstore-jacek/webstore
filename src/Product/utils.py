from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

from xhtml2pdf import pisa
from io import BytesIO

from .models import Product

def sort_id(val):
        return val.id

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.decode("utf-8").encode("iso-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def find_customers(phrase):
    ret = []
    data = phrase.strip().split(' ')
    for n, word in enumerate(data):
        ret.append(set())
        ret[n].update(list(Customer.objects.filter(name__icontains=word)))
    return list(reduce(lambda a, b: a & b, ret))