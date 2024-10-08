from django import forms
from django.contrib.auth.models import User
from recordApp.models import course_register, cbt, questions

class courseAddForm(forms.ModelForm):
    course = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Title',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Title')
    unit = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Course Unit',
            'class':'form-control shadow-sm border-1',
        }), label='Course Unit')
    course_code = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Code',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Code')
    level = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Level',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Level')
    instructor = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Lecturer Incharge',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Lecturer Incharge')
    
    class Meta:
        model = course_register
        fields = [
            'course', 'course_code', 'unit', 'level','instructor'
        ]

class courseEditForm(forms.ModelForm):
    course = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Title',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Title')
    unit = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Course Unit',
            'class':'form-control shadow-sm border-1',
        }), label='Course Unit')
    course_code = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Code',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Code')
    level = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Level',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Level')
    instructor = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Lecturer Incharge',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Lecturer Incharge')
    class Meta:
        model = course_register
        fields = [
            'course', 'course_code', 'unit', 'level', 'instructor'
        ]

class reg_cbt(forms.ModelForm):
    course_title = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Title',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Title')
    course_code = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Code',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Code')
    execution_time = forms.TimeField(widget=forms.TimeInput(attrs={
            'class':'form-control shadow-sm border-1',
            'type':'time'
        }), label='Execution Time')
    execution_date= forms.DateField(widget=forms.DateInput(attrs={
            'class':'form-control shadow-sm border-1',
            'type':'date'
        }), label='Execution Date')
    class Meta:
        model = cbt
        fields = [
            'course_title', 'course_code', 'execution_time', 'execution_date'
        ]