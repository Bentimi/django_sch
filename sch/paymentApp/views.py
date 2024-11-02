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
from rave_python import Rave, RaveExceptions, Misc
from django.urls import reverse
from django.core.mail import send_mail


# Create your views here.

@login_required
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
                # invoice_table.objects.create(user_id=request.user.id)
                inv = invoice_table.objects.filter(user_id=user_id, status='unsuccessful').order_by('-invoice_id').first()
                if inv:
                    inv_info = invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id)
                    if inv_info:
                        for invoice in inv_info:
                            if status == 'late_reg':
                                 invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Late Registration', amount=fee.late_reg_fee, category=status  )
                            elif status == 'reg_form':
                                 invoice_table.objects.filter(user_id=user_id, status='unsuccessful', invoice_id=inv.invoice_id).update(transaction_type='Admission Form Fee', amount=fee.admission_form_fee, category=status)
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

amount_charged=0.0      
@login_required
def paymentConfirm(request, user_id, status):
    invoice = invoice_table.objects.all().filter(user_id=user_id, status='unsuccessful', category=status).order_by('invoice_id').last()
    user  = User.objects.all().filter(id=user_id) 
    global amount_charged
    amount_charged =invoice.amount

    return render(request, 'paymentApp/invoice.html',{
            'invoice':invoice,
            'status':status,
            'user_profile':user
    })

@login_required       
def cancelPayment(request, inv_id, status):
    invoice_table.objects.filter(invoice_id=inv_id, status='unsuccessful').delete()
    return redirect('payment_details', request.user.id, status)

@login_required
def makePayment(request, inv_id):
    if request.method == "POST":
      
       user = User.objects.get(id=request.user.id)
       form = Payment_form(request.POST)
       if form.is_valid():
           card_num = form.cleaned_data['card_number']
           cvv = form.cleaned_data['cvv']
           exp_date = form.cleaned_data['expire_date']

           print(f'''
                     Card Num: {card_num} 
                     CVV: {cvv} 
                     Exp Date: {exp_date} 
            ''')
           rave = Rave("FLWPUBK_TEST-d31102d086dd9cebe66f5f0b137e0112-X", "FLWSECK_TEST-cedf324409d9a2df2fd6bdd329150811-X", usingEnv = False)

            # Payload with pin
           payload = {
            "cardno": str(card_num),
            "cvv": str(cvv),
            "expirymonth": str(exp_date).split("/")[0],
            "expiryyear": str(exp_date).split("/")[1],
            "amount": amount_charged,
            "email": user.email,
            "phonenumber": user.profile.phone_no,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "IP": "355426087298442",
            }
           try:
                res = rave.Card.charge(payload)

                if res["suggestedAuth"]:
                    arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

                    if arg == "pin":
                        Misc.updatePayload(res["suggestedAuth"], payload, pin="3310")
                    if arg == "address":
                        Misc.updatePayload(res["suggestedAuth"], payload, address= {"billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})
                    
                    res = rave.Card.charge(payload)

                if res["validationRequired"]:
                    rave.Card.validate(res["flwRef"], "")

                res = rave.Card.verify(res["txRef"])
                messages.success(request, ('Payment Successful.'))
                return HttpResponsePermanentRedirect(reverse('payment_success', args=(inv_id,)))

           except RaveExceptions.CardChargeError as e:
                messages.error(request, ('Charge Fails.'))
                return HttpResponsePermanentRedirect(reverse('payment_fails', args=(inv_id,)))

           except RaveExceptions.TransactionValidationError as e:
                messages.error(request, ('TransactionFails.'))
                return HttpResponsePermanentRedirect(reverse('payment_fails', args=(inv_id,)))

           except RaveExceptions.TransactionVerificationError as e:
                messages.error(request, ('Validation Fails.'))
                return HttpResponsePermanentRedirect(reverse('payment_fails', args=(inv_id,)))
       else:
            messages.error(request, ('Some fields are not correctly filled!'))
            return HttpResponsePermanentRedirect(reverse('payment_fails', args=(inv_id)))


    else:
        form = Payment_form()
        inv=invoice_table.objects.filter(invoice_id=inv_id)
        if inv:
            for invoice in inv:
                status = invoice.category
    return render(request, 'paymentApp/flutter_pay.html', {
        'form':form,
        'inv_id':inv_id,
        'status':status,
        'amount':amount_charged
        })

@login_required
def paymentSuccess(request, inv_id):
    inv=invoice_table.objects.all().filter(invoice_id=inv_id)
    if inv:
        for invoice in inv:
            status = invoice.transaction_type
            invoice_table.objects.filter(invoice_id=inv_id).update(completed=True, status='successful')
            invoice_table.objects.filter(user_id=request.user.id,status='unsuccessful').delete()
            if invoice.category == 'reg_form':
                if admission_invoice_table.objects.all().filter(invoice_id=invoice.invoice_id).exists():
                    admission_invoice_table.objects.all().filter(invoice_id=invoice.invoice_id).update(user_id=request.user.id)
                else:
                    admission_invoice_table.objects.create(invoice_id=invoice.invoice_id,form_fee=invoice.transaction_type, paid=True).DoesNotExist()
                    invoice_details=admission_invoice_table.objects.only('paid').get(invoice_id=invoice.invoice_id)
                    if invoice_details.paid == True:
                        admission_invoice_table.objects.all().filter(invoice_id=invoice.invoice_id).update(user_id=request.user.id)
                # if invoice_details.invoice_id == invoice.invoice_id:
                #  admission_invoice_table.objects.filter(invoice_id=invoice.invoice_id, form_fee=invoice.transaction_type, paid=True).update(aspirant_id=invoice.user_id,)
    # Send Mail to user
            send_mail(
                f'{status} Fee', # Subject of the mail
                f'{status} Payment successfully made!', # Body of the mail
                'gradschool@gmail.com', # From email (sender)
                [request.user.email],  # To email (Receiver)
                fail_silently = False, # Handle any error
            )
    # messages.success(request, ('Your payment was successful!'))
    return render(request, 'paymentApp/successful_payment.html', {
        'inv':inv
    })

@login_required
def paymentFail(request, inv_id):
    inv=invoice_table.objects.filter(invoice_id=inv_id)
    if inv:
        for invoice in inv:
            status = invoice.transaction_type
    # Send Mail to user
            send_mail(
                f'{status} Fee', # Subject of the mail
                'Payment Fails!', # Body of the mail
                'gradschoo@gmail.com', # From email (sender)
                [request.user.email],  # To email (Receiver)
                fail_silently = False, # Handle any error
            )
    messages.error(request, ('Transaction Fails!'))
    return makePayment(request, inv_id)


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