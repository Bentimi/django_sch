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
    if fees_:
        for fee in fees_:
            if status == 'tuition':
                if request.method == "POST":
                    tuition_form = tuitionForm(request.POST)
                    if tuition_form.is_valid():
                        tuition_trans = tuition_form.cleaned_data['transaction_type']
                        print(tuition_trans)
                        
                        invoice_table.objects.create(user_id=request.user.id)

                        inv = invoice_table.objects.filter(user_id=user_id, status='unsuccessful').order_by('-invoice_id').first()
                        if inv:
                            inv_info = invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id)

                            if inv_info:
                                for invoice in inv_info:
                                    if tuition_trans == 'Full Payment':
                                    
                                        invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Full Payment', amount=fee.Full_tuition_fee, category=status)

                                    elif tuition_trans == 'Part Payment':
                                        invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Part Payment', amount=fee.part_tuition_fee, category=status)
                                return redirect('payment_confirm', request.user.id, status)
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
            
            else:
                invoice_table.objects.create(user_id=request.user.id)
                inv = invoice_table.objects.filter(user_id=user_id, status='unsuccessful').order_by('-invoice_id').first()
                if inv:
                    inv_info = invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id)
                    if inv_info:
                        for invoice in inv_info:
                            if status == 'late_reg':
                                 invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Late Registration', amount=fee.late_reg_fee, category=status  )
                            elif status == 'reg_form':
                                 invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Admission Form Fee', amount=fee.admission_form_fee, category=status   )
                    return render(request, 'paymentApp/payment_details.html',{
                                'user_profile':user_info,
                                'status':status,
                                'fee':fees_,
                                'inv':inv
                            })
            return render(request, 'paymentApp/payment_details.html',{
                'user_profile':user_info,
                'status':status,
                'fee':fees_,
            })
        
def paymentConfirm(request, user_id, status):
    invoice = invoice_table.objects.all().filter(user_id=user_id, status='unsuccessful', category=status).order_by('invoice_id').last()  

    return render(request, 'paymentApp/invoice.html',{
            'invoice':invoice,
            'status':status
    })
        
def cancelPayment(request, inv_id, status):
    invoice_table.objects.filter(invoice_id=inv_id).delete()
    return redirect('payment_details', request.user.id, status)


def makePayment(request, inv_id):
    if request.method == "POST":
      
       user = User.objects.get(id=request.user.id)
       form = Payment_form(request.POST or None)
       if form.is_valid():
           card_num = form.cleaned_data['card_number']
           cvv = form.cleaned_data['cvv']
           exp_date = form.cleaned_data['esxpire_date']

           print(f'''
                     Card Num: {card_num} 
                     CVV: {cvv} 
                     Exp Date: {exp_date} 
            ''')
           

    else:
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