from django.urls import include, path, re_path
from userApp import views

urlpatterns = [
    re_path(r'^nav_bar/(?P<user_id>\d+)/', views.navBar, name='nav_bar'),
    re_path(r'^profile/(?P<user_id>\d+)/', views.displayProfile, name='profile'),
    re_path(r'^edit_profile/(?P<user_id>\d+)/', views.editProfile, name='edit_profile'),
    re_path(r'^deactivate_profile/(?P<user_id>\d+)/', views.deactivateProfile, name='deactivate_profile'),
    re_path(r'^view_users/(?P<user>\w+)/', views.viewUsers, name='view_users'),
    re_path(r'^delete_user/(?P<user_id>\d+)/', views.deleteUser, name='delete_user'),
    re_path(r'^user_verification/(?P<user>\w+)/', views.userVerification, name='user_verification'),
    re_path(r'^doc_approval_identity/(?P<user_id>\d+)/', views.docApproval_identity, name='doc_approval_identity'),
    re_path(r'^doc_approval_particulars/(?P<user_id>\d+)/', views.docApproval_paritculars, name='doc_approval_particulars'),
    re_path(r'^delete_particulars/(?P<user_id>\d+)/', views.deleteParticulars, name='delete_particulars'),
    re_path(r'^delete_identity/(?P<user_id>\d+)/', views.deleteIdentity, name='delete_identity'),
    re_path(r'^count_down/', views.countDown, name='count_down'),
]