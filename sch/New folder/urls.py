from django.urls import include, path, re_path
from recordApp import views

urlpatterns = [
    re_path(r'^course_setup/', views.courseSetup, name='course_setup'),
    re_path(r'^view_course/', views.displayCourses, name='view_course'),
    re_path(r'^course_details/(?P<course_id>\d+)/', views.courseDetails, name='course_details'),
    re_path(r'^edit_course/(?P<course_id>\d+)/', views.editCourse, name='edit_course'),
    re_path(r'^delete_course/(?P<course_id>\d+)/', views.deleteCourse, name='delete_course'),
    re_path(r'^cbt_reg/(?P<user>\d+)/', views.cbtReg, name='cbt_reg'),
    re_path(r'^test_details/', views.cbtDetails, name='test_details'),
]