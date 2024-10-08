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
    no_of_questions = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder':'Number of Questions',
            'class':'form-control shadow-sm border-1',
        }), label='Number of Questions')
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
            'no_of_questions','execution_time', 'execution_date'
        ]

class course_details(forms.ModelForm):
    course = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Title',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Title', disabled=True)
    course_code = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Course Code',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Course Code', disabled=True)
    class Meta:
        model = course_register
        fields = [
            'course', 'course_code'
        ]

class question_form(forms.ModelForm):
    class Meta:
        model = questions
        fields = [
            'question', 'first_option', 'second_option', 'third_option', 'forth_option', 'answer'
        ]