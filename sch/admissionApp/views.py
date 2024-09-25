from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import admissionForm
from django.contrib.auth.models import User
from .models import aspirants_profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
import bcrypt

# pwd = input('password: ')
# password = pwd.encode('utf-8')

# hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# print(f'Hashed Password: {hashed_password}')

# login = input('Password: ')
# login_pwd = login.encode('utf-8')

# if bcrypt.checkpw(login_pwd, hashed_password):
#     print('Correct!')
# else:
#     print('Error!')

def admissionReg(request):
    if request.method == "POST":
        pwd = request.POST['pWd'].strip()
        password = request.POST['password'].strip()
        reg_form = admissionForm(request.POST or None, request.FILES or None)
        if reg_form.is_valid():
            if pwd == password:
                reg = reg_form.save(commit=False)
                pass_word = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(pass_word, bcrypt.gensalt())
                reg.password = hashed_password
                reg.save()
                messages.success(request, ('Candidate Successfully Registered!'))
                return redirect("admission_reg")
            else:
                messages.error(request, ('Passwords are not the same!'))
                return redirect("admission_reg")
    else:
        reg_form = admissionForm()
    return render(request, 'admissionApp/registration.html', {'form': reg_form})

@login_required
def registeredForms(request):
    registered_forms = aspirants_profile.objects.all()
    return render(request, 'admissionApp/registered_users.html', {'all_reg':registered_forms})

@login_required
def viewProfile(request, user_id):
    profile = aspirants_profile.objects.all().filter(aspirant_id=user_id)
    return render(request, 'admissionApp/view_profile.html', {'my_profile':profile})