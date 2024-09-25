from django.urls import include, path, re_path
from admissionApp import views

urlpatterns = [
    re_path(r'^admission_reg/', views.admissionReg, name='admission_reg'),
    re_path(r'^registered_users/', views.registeredForms, name='registered_users'),
    re_path(r'^aspirant_profile/(?P<user_id>\d+)', views.viewProfile, name='aspirant_profile'),
]