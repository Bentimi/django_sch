from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from paymentApp.forms import Payment_form, tuitionForm
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.contrib.auth.models import User
from adminApp.models import fees_table
from paymentApp.models import invoice_table, admission_invoice_table, tuition_invoice_table, lateReg_invoice_table

# Create your views here.

def paymentDetails(request, user_id, status):
    user_info = User.objects.all().filter(id=user_id)
    fees_ = fees_table.objects.all()
    if status == 'tuition':
        if request.method == "POST":
            tuition_form = tuitionForm(request.POST)
            if tuition_form.is_valid():
                tuition_trans = tuition_form.cleaned_data['transaction_type']
                print(tuition_trans)
                
                invoice_table.objects.create(user_id=request.user.id)
                if fees_:
                    for fee in fees_:
                        inv = invoice_table.objects.filter(user_id=user_id, status='unsuccessful').order_by('-invoice_id').first()
                        if inv:
                            inv_info = invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id)

                            if inv_info:
                                for invoice in inv_info:
                                    if tuition_trans == 'Full Payment':
                                    
                                        invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(tran)

                                    elif tuition_trans == 'Part Payment':
                                        print(fee.part_tuition_fee)
                        return render(request, 'paymentApp/payment_details.html',{
                                'user_profile':user_info,
                                'status':status,
                                'fee':fees_,
                                'tuition_form':tuition_form,
                                'inv':inv
                            })
        else:
            tuition_form = tuitionForm()
        return render(request, 'paymentApp/payment_details.html',{
            'user_profile':user_info,
            'status':status,
            'fee':fees_,
            'tuition_form':tuition_form
        })
    

    return render(request, 'paymentApp/payment_details.html',{
        'user_profile':user_info,
        'status':status,
        'fee':fees_,
    })

def makePayment(request, inv_id):
    form = Payment_form()
    return render(request, 'paymentApp/flutter_pay.html', {'form':form})



def render_to_pdf(template_src, context_dict={}):
    pass
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('Error rendering PDF', status=500)
#     return response

def viewPDF(request):
    pass
#     context = {'title': 'My PDF Report', 'data': 'This is dynamic content!'}
#     return render_to_pdf('paymentApp/pdf_template.html', context)

def downloadPDF(request):
    pass