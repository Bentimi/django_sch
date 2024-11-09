from django.urls import include, path, re_path
from recordApp import views

urlpatterns = [
    re_path(r'^course_setup/', views.courseSetup, name='course_setup'),
    re_path(r'^view_course/', views.displayCourses, name='view_course'),
    re_path(r'^course_details/(?P<course_id>\d+)/', views.courseDetails, name='course_details'),
    re_path(r'^edit_course/(?P<course_id>\d+)/', views.editCourse, name='edit_course'),
    re_path(r'^delete_course/(?P<course_id>\d+)/', views.deleteCourse, name='delete_course'),
    re_path(r'^cbt_reg/(?P<user_id>\d+)/', views.cbtReg, name='cbt_reg'),
    re_path(r'^test_details/(?P<user_id>\d+)/', views.cbtDetails, name='test_details'),
    re_path(r'^test_questions/(?P<user_id>\d+)/', views.cbtQuestions, name='test_questions'),
    re_path(r'^view_questions/(?P<user_id>\d+)/', views.viewQuestions, name='view_questions'),
    re_path(r'^edit_questions/(?P<user_id>\d+)/', views.editQuestions, name='edit_questions'),
    re_path(r'^cbt_test/(?P<test_id>\d+)/', views.cbtTest, name='cbt_test'),
    # re_path(r'^cbt_testsubmit/(?P<test_id>\d+)/', views.cbtTestsubmit, name='cbt_testsubmit'),
    re_path(r'^course_reg/(?P<user_id>\d+)/', views.courseReg, name='course_reg'),
    re_path(r'^add_course/(?P<course_id>\d+)/', views.addCourses, name='add_course'),
    re_path(r'^remove_course/(?P<course_id>\d+)/', views.removeCourses, name='remove_course'),
    re_path(r'^course_form/(?P<user_id>\d+)/', views.courseForm, name='course_form'),
    re_path(r'^available_test/(?P<user_id>\d+)/', views.avaliableTest, name='available_test'),
    re_path(r'^confirm_test/(?P<test_id>\d+)/', views.confirmTest, name='confirm_test'),
    re_path(r'^result/(?P<user_id>\d+)/', views.viewResult, name='result'),
]