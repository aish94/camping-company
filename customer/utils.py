from io import BytesIO
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
from customer.models import Pdf

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
    if not pdf.err:
        # Pdf(pdf=result.getvalue()).save()
        return redirect("app:findus")
    return None