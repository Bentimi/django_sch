from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import admissionForm, registrationForm, profile_registrationForm, reg_profileForm, loginForm, confirmationForm, edit_userForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import aspirants_profile, admission_approval
from userApp.models import users_status, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect


def admissionReg(request):
    form = registrationForm()

    if request.method == "POST":
        form = registrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, ('Candidate Successfully Registered!'))
            return redirect('admission_login')
        else:
            messages.error(request, ('please correct the error below.'))
            return redirect('admission_reg')

    context = {'reg_form':form}
    return render(request, 'admissionApp/registration.html', context=context)
   
def admissionLogin(request):
    # form = loginForm()
    if request.method == "POST":
        login_form = loginForm(request, data=request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request , username=username, password=password)

            if user is not None:
                login(request, user)
                if request.user.is_authenticated and not request.user.is_superuser:
                    status = users_status.objects.all().filter(user_id=request.user.id)
                    for x in status:
                        if x.aspirant is not True:
                            users_status.objects.all().filter(user_id=request.user.id).update(aspirant=True)
                            aspirants_profile.objects.create(user_id=request.user.id)
                    return redirect('dashboard')
                elif  request.user.is_authenticated and request.user.is_superuser:
                    messages.success(request, ('superuser'))
                    return redirect('admission_login')
                    
            
    
        else:
            messages.error(request, ('Invalid username or password'))
            return redirect('admission_login')
        
    else:
        form = loginForm()
        return render(request, 'admissionApp/login.html', {'form':form})

@login_required(login_url=(admissionLogin))
def admissionLogout(request):
    logout(request)
    messages.success(request, ('Successfully Logged Out!'))
    return redirect('admission_login')

@login_required
def registeredForms(request):
    registered_forms = aspirants_profile.objects.all().filter(registration_status=True)
    registered_forms_agg = aspirants_profile.objects.all().filter(registration_status=True).count
    admitted_agg = admission_approval.objects.all().filter(status=True).count
    # if registered_forms:
    #     for reg in registered_forms:
    #         approval = reg.aspirant_id
    # pk = 
    # aspirants_id = aspirants_profile.objects.all().filter(user_id=pk)
    # for aspirant in aspirants_id:
    #      approval = admission_approval.objects.all().filter(aspirant_id=aspirant.aspirant_id)
    
    return render(request, 'admissionApp/registered_users.html', {
        'all_reg':registered_forms,
        'agg':registered_forms_agg,
        'admission':admitted_agg,
        # 'approval':approval
        })

@login_required
def viewProfile(request, user_id):
    global pk 
    pk = user_id
    profile = User.objects.all().filter(id=user_id)
    reg_profile = aspirants_profile.objects.all().filter(user_id=user_id)
    context = {
        'my_profile':profile,
       'registration_profile':reg_profile,
        }
    return render(request, 'admissionApp/view_profile.html', context=context)

@login_required
def profileDashboard(request):
    user_id = request.user.id
    all_profile = User.objects.all().filter(id=user_id)
    registration_profile = aspirants_profile.objects.filter(user=user_id)
    context = {
        'my_profile':all_profile,
        'registration_profile':registration_profile,
        }
    return render(request, 'admissionApp/dashboard.html', context=context)

@login_required
def profileDashboardEdit(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    user = get_object_or_404(aspirants_profile, user=user_id)
    if request.method == "POST":
        profile_form = reg_profileForm(request.POST or None, request.FILES or None, instance=user_info.profile)
        admission_form = admissionForm(request.POST or None, request.FILES or None, instance=user)
        
        if profile_form.is_valid() and admission_form.is_valid():
            with transaction.atomic():
                profile_form.save()
                admission_form.save()
                aspirants_profile.objects.filter(user=user_id).update(registration_status=True)
            return redirect('dashboard')
        else:
            messages.error(request, ('please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('dashboard_edit', args=(user_id,)))
    else:
        profile_form = reg_profileForm(instance=user_info.profile)
        user_info = edit_userForm(instance=user_info)
        admission_form = admissionForm(instance=user)
        status = users_status.objects.all().filter(user_id=user_id)
        profile = User.objects.all().filter(id=user_id)
        reg_status = aspirants_profile.objects.all().filter(user_id=user_id)
        context = {
            'profile_form' : profile_form,
            'user' : user_info,
            'status' : status,
            'my_profile' : profile,
            'admission_form' : admission_form,
            'reg_status' : reg_status,
        }
        return render(request, 'admissionApp/edit_profile.html', context=context)

@login_required
def admissionApproval(request, user_id):
     profile = aspirants_profile.objects.all().filter(user_id=user_id)
     if profile:
        for user in profile:
            aspirant = user.aspirant_id
            approval_status = admission_approval.objects.all().filter(aspirant_id=aspirant)
            if approval_status.exists():
                admission_approval.objects.update( officer_incharge_id=request.user.id, status=True)
            else:
                admission_approval.objects.create(aspirant_id=aspirant)
                admission_approval.objects.update( officer_incharge_id=request.user.id, status=True)
                messages.success(request, ('Candidate admission secured!'))


        # print(approval.)
        # if request.user.is_superuser:
        #     if approval.exists:
        #         pass
        #     else:
        #         admission_approval.objects.update(aspirant_id=aspirant_id)
                # messages.success(request, ('Candidate admission secured!'))
        #         return HttpResponsePermanentRedirect(reverse('aspirant_profile', args=(user_id,)))
     return viewProfile(request, user_id)

@login_required
def admissionLetter(request, user_id):
    profile = User.objects.all().filter(id=user_id)
    other_info = aspirants_profile.objects.all().filter(user_id=user_id)

    context = {
        'all_profile':profile,
        'info' : other_info
    }
    return render(request, 'admissionApp/admission_letter.html', context=context)

