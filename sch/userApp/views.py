from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, User_update_form, Profile_update_form
from django.contrib.auth.models import User
from .models import Profile, users_status
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
import time
import random
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.contrib.auth import logout
from admissionApp.models import aspirants_profile

# Create your views here.
    
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def navBar(request, user_id):
    profile = User.objects.all().filter(id=user_id)
    aspirant = aspirants_profile.objects.all().filter(user_id=request.user.id)
    return render(request=request,
                  template_name='userApp/nav_bar.html',
                  context={'my_profile' : profile, 'aspirant':aspirant})

# @login_required
def sideBar(request):
    profile = User.objects.all().filter(id=request.user.id)
    aspirant = aspirants_profile.objects.all().filter(user_id=request.user.id)
    return render(request, 'userApp.side_nav.html',
                  context={
                      'my_profile' : profile, 'aspirant':aspirant,
                      'aa':'hello'
                      })

@login_required
def userDashboard(request):
    user = User.objects.all().filter(id=request.user.id)
    if user:
     for profile in user:
         if profile.users_status.aspirant is True and not profile.users_status.student is True:
             return redirect('dashboard')
         else:
            return render(request, 'userApp/dashboard.html', {
                    'user_profile':user
                })

@login_required
def displayProfile(request, user_id):
    profile = User.objects.all().filter(id=user_id)
    random_val = random.randint(1000, 9999)
    matric_year = time.strftime('%y',)
    matric_no = (f'{matric_year}{random_val}')
    return render(request=request,
                  template_name='userApp/display_profile.html',
                  context={'my_profile' : profile, 'matric_no':matric_no})

@login_required
def editProfile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user_form = User_update_form(request.POST, instance=user)
        profile_form = Profile_update_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
                
                if profile_form.cleaned_data['staff']:
                    user.is_staff = True
                    user.save()
                    users_status.objects.filter(user_id=user_id).update(staff=True)
                else:
                    user.is_staff = False
                    user.save()
                    users_status.objects.filter(user_id=user_id).update(staff=False)
            messages.success(request, ('Your profile was successfilly updated!'))
            return HttpResponsePermanentRedirect(reverse('profile', args=user_id))
        else:
            messages.error(request, ('please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(user_id,)))
    else:
        user_form = User_update_form(instance=user)
        profile_form = Profile_update_form(instance=user.profile)
        profile = User.objects.get(id=user_id)
        return render(request, 'userApp/edit_profile_form.html', {
            'user_form' : user_form,
            'profile_form' : profile_form,
            'profile' : profile
        })

@login_required
def deactivateProfile(request, user_id):
    user = User.objects.only("is_active").get(id=user_id)
    if user.is_active:
        User.objects.filter(id=user_id).update(is_active=False)
    else:
        User.objects.filter(id=user_id).update(is_active=True)
    return displayProfile(request, user_id)

status = ""
@login_required
def viewUsers(request, user):
    global status
    status = user
    if status == 'staff':
        users = users_status.objects.all().filter(staff=True, student=False)
        users_agg = users_status.objects.all().filter(staff=True, student=False).count
    else:
        users = users_status.objects.all().filter(staff=False, student=True)
        users_agg = users_status.objects.all().filter(staff=False, student=True).count
        # user_status = users_status.objects.all().filter(student=True)
    return render(request, 'userApp/view_users.html', 
                  {
                      "users" : users, 
                      "status" : status,
                      "users_agg":users_agg
                      })

@login_required
def deleteUser(request, user_id):
    Profile.objects.all().filter(user_id=user_id).delete()
    User.objects.all().filter(id=user_id).delete()
    messages.success(request, ("Profile Successfully Deleted!"))
    return viewUsers(request, status)

verification = ""
@login_required
def userVerification(request, user):
    global Verification
    Verification = user
    if user == 'verified':
       user_info =  Profile.objects.all().filter(staff=True, means_of_identity_approval="Approved", particulars_approval="Approved")
    else:
         user_info =  Profile.objects.filter(staff=True).exclude(means_of_identity_approval="Approved", particulars_approval="Approved")
    return render(request, 'userApp/doc_verify.html', {'users':user_info})

@login_required
def docApproval_identity(request, user_id):
    approve_document = Profile.objects.get(user_id=user_id)
    if approve_document.means_of_identity_approval == "Approved":
        Profile.objects.filter(user_id=user_id).update(means_of_identity_approval="Unapproved")
    else:
         Profile.objects.filter(user_id=user_id).update(means_of_identity_approval="Approved")
    return userVerification(request, verification)

@login_required
def docApproval_paritculars(request, user_id):
    approve_document = Profile.objects.get(user_id=user_id)
    if approve_document.particulars_approval == "Approved":
        Profile.objects.filter(user_id=user_id).update(particulars_approval="Unapproved")
    else:
         Profile.objects.filter(user_id=user_id).update(particulars_approval="Approved")
    return userVerification(request, Verification)

@login_required
def deleteParticulars(request, user_id,):
    profile = Profile.objects.filter(user_id=user_id)
    if profile.particulars:
        Profile.objects.filter(user_id=user_id).update(particulars='')
    return docApproval_paritculars(request, user_id)


@login_required
def deleteIdentity(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    if profile.means_of_identity:
        Profile.objects.filter(user_id=user_id).update(means_of_identity='',means_of_identity_approval="Uapproved", particulars_approval="Unapproved")
    return docApproval_paritculars(request, user_id)

def countDown(request):
    target_date = datetime(2024, 11, 30, 0, 0)
    date_now = datetime.now()
    time_remaining = target_date - date_now

    context = {
        'days' : f'{time_remaining.days:02}',
        'hrs' : f'{time_remaining.seconds // 3600:02}',
        'mins' : f'{(time_remaining.seconds % 3600) // 60:02}',
        'secs' : f'{time_remaining.seconds % 60:02}',
    }
    return render(request, 'about.html', context=context)