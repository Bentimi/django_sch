from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class course_model(models.Model):
    course_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    course = models.CharField(max_length=100, unique=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, unique=False)

class course_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    course_model = models.ForeignKey(course_model, on_delete=models.CASCADE, unique=False, null=True)
    instructor = models.CharField(max_length=500, unique=False)
    course = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=30, unique=True, null=True)
    unit = models.CharField(max_length=10, unique=False) 
    level = models.CharField(max_length=10, unique=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True, unique=False)
    last_update = models.CharField(blank=True, unique=False, null=True, max_length=50)

class cbt(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(course_register, on_delete=models.CASCADE, unique=False, null=True)
    course_title = models.CharField(unique=True, max_length=200, null=True)
    course_code = models.CharField(max_length=30, unique=True, null=True)
    duration = models.PositiveIntegerField(unique=False, null=True)
    # execution_time = models.TimeField(max_length=50, unique=False, null=True)
    execution_date = models.DateTimeField(max_length=50, unique=False, null=True)
    no_of_questions = models.CharField(max_length=500, unique=False, null=True)
    examiner = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

class questions(models.Model):
    id = models.AutoField(primary_key=True)
    cbt = models.ForeignKey(cbt, on_delete=models.CASCADE, unique=False, null=True)
    question = models.CharField(max_length=500, unique=False, null=True)
    first_option = models.CharField(max_length=500, unique=False, null=True)
    second_option = models.CharField(max_length=500, unique=False, null=True)
    third_option = models.CharField(max_length=500, unique=False, null=True)
    forth_option = models.CharField(max_length=500, unique=False, null=True)
    answer = models.CharField(max_length=500, unique=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

class grading(models.Model):
    grade_id = models.AutoField(primary_key=True)
    cbt = models.ForeignKey(cbt, on_delete=models.CASCADE, unique=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    score = models.CharField(max_length=20, unique=False, null=True)
    active = models.BooleanField(unique=False, default=False)
    submitted = models.BooleanField(unique=False, default=False)
    executed_time = models.DateTimeField(auto_now_add=True, unique=False)
    finished_time = models.CharField(max_length=100, unique=False, null=True, blank=True)

class course_form(models.Model):
    course_form_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(course_register, on_delete=models.CASCADE, unique=False, null=True)
    cbt = models.ForeignKey(cbt, on_delete=models.CASCADE, unique=False, null=True)
    score = models.ForeignKey(grading, on_delete=models.CASCADE, unique=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    units = models.CharField(max_length=10, unique=False, null=True)
    level = models.CharField(max_length=10, unique=False, null=True)
    status = models.BooleanField(default=False, unique=False)
    date_added = models.DateTimeField(auto_now_add=True)
