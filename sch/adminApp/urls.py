from django.urls import include, path, re_path
from adminApp import views

urlpatterns = [
    re_path(r'^fees_form/', views.feesForm, name='fees_form'),
    re_path(r'^display_fees/', views.displayFees, name='display_fees'),
    re_path(r'^view_fees/(?P<fees_id>\d+)/(?P<fee>\w+)/', views.viewFees, name='view_fees'),
    re_path(r'^edit_fees/(?P<fees_id>\d+)/(?P<fee>\w+)/', views.editFees, name='edit_fees'),
]