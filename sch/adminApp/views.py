from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from adminApp.forms import feesRegForm, edit_admissionFee, edit_lateReg, edit_tuition
from adminApp.models import fees_table

# Create your views here.

def feesForm(request):
    if request.method == "POST":
        form = feesRegForm(request.POST)
        if form.is_valid():
           fee = form.save(commit=False)
           fee.user_id = request.user.id
           fee.save()
           messages.success(request, 'Saved')
        return displayFees(request)
    else:
        form = feesRegForm()
    return render(request, 'adminApp/fees_form.html', {'form':form})

def displayFees(request):
    all_fees = fees_table.objects.all()
    return render(request, 'adminApp/display_fees.html', {'all_fees':all_fees})

def viewFees(request, fees_id, fee):
   status = fee
   all_fees = fees_table.objects.all().filter(id=fees_id)
   return render(request, 'adminApp/view_fee.html', {'all_fees':all_fees, 'status':fee})

def editFees(request, fees_id, fee):
    id_ = get_object_or_404(fees_table, id=fees_id)
    # get_id = fees_table.objects.all().filter(id=id_) 
    if request.method == "POST":
        tuition_form = edit_tuition(request.POST, instance=id_)
        late_reg = edit_lateReg(request.POST, instance=id_)
        admission_fee = edit_admissionFee(request.POST, instance=id_)
        if tuition_form.is_valid():
            tuition_form.save()
        elif  late_reg.is_valid():
            late_reg.save()
        elif  admission_fee.is_valid():
            admission_fee.save()
        return viewFees(request, fees_id, fee)
    else:
        tuition_form = edit_tuition(instance=id_)
        late_reg = edit_lateReg(instance=id_)
        admission_fee = edit_admissionFee(instance=id_)
    return render(request, 'adminApp/edit_fee.html', 
                    {
                    'status':fee,
                    'tuition':tuition_form,
                    'late_reg':late_reg,
                    'admission_fee':admission_fee
                    }
                        )