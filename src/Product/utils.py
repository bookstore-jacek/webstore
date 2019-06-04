from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

from xhtml2pdf import pisa

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     #result = StringIO()
#     #pdf = pisa.CreatePDF(StringIO(html.encode('utf-8')), result)    
#     pdf = pisa.CreatePDF(html.encode('UTF-8'), result, encoding='UTF-8')    #     StringIO(html),
#     #     dest=result,
#     #     encoding='UTF-8'
#     # )    

#     # template = get_template(template_src)
#     # context_dict['STATIC_ROOT'] = settings.STATIC_ROOT
#     # context_dict['pdf'] = '1'
#     # context = context(context_dict)
#     # html = template.render(context)
#     # # return HttpResponse(html)
#     # result = StringIO()
#     # pdf = pisa.CreatePDF(StringIO(html.encode('utf-8')), result)

#     # if not pdf.err:
#     #     return HttpResponse(result.getvalue(), content_type='application/pdf')
#     # return None



from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.decode("utf-8").encode("iso-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None