from django.urls import include, path, re_path
from admissionApp import views

urlpatterns = [
    re_path(r'^admission_reg/', views.admissionReg, name='admission_reg'),
    re_path(r'^admission_login/', views.admissionLogin, name='admission_login'),
    re_path(r'^admission_logout/', views.admissionLogout, name='admission_logout'),
    re_path(r'^registered_users/', views.registeredForms, name='registered_users'),
    re_path(r'^aspirant_profile/(?P<user_id>\d+)/', views.viewProfile, name='aspirant_profile'),
    re_path(r'^dashboard/', views.profileDashboard, name='dashboard'),
    re_path(r'dashboard_edit/(?P<user_id>\d+)/', views.profileDashboardEdit, name='dashboard_edit'),
    re_path(r'admission_approved/(?P<user_id>\d+)/', views.admissionApproval, name='admission_approved'),
    re_path(r'admission_deny/(?P<user_id>\d+)/', views.admissionDenied, name='admission_deny'),
    re_path(r'admission_letter/(?P<user_id>\d+)/', views.admissionLetter, name='admission_letter'),
]