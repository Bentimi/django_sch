from django import forms
from django.contrib.auth.models import User
from recordApp.models import course_register, cbt, questions, course_form, grading

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
        }), label='Lecturer Incharge (Username)')
    
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
        }), label='Lecturer Incharge (Username)')
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
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder':'Duration',
            'class':'form-control shadow-sm border-1',
            'type':'number'
        }), label='Duration')
    execution_date= forms.DateTimeField(widget=forms.DateTimeInput(attrs={
            'class':'form-control shadow-sm border-1',
            'type':'datetime-local'
        }), label='Execution Date')
    approved = forms.BooleanField(widget=forms.CheckboxInput(attrs={
       'class':'shadow-sm border-1 form-check-input'
    }),required=False, label='Test Approval')
    class Meta:
        model = cbt
        fields = [
            'no_of_questions','duration', 'execution_date', 'approved'
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
    question = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Question',
            'class':'form-control shadow-sm border-1',
            'cols':'5',
            'rows':'6',
        }), label='Question')
    first_option = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'First Option',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='First Option')
    second_option = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Second Option',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Second Option')
    third_option = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Third Option',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Third Option')
    forth_option = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Forth Option',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Forth Option')
    answer = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Answer',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Answer')
    class Meta:
        model = questions
        fields = [
            'question', 'first_option', 'second_option', 'third_option', 'forth_option', 'answer'
        ]

class test_form(forms.Form):
     answer = forms.CharField(widget=forms.TextInput(attrs={
            'type' : 'text'
        }), label='Answer')
     
class resultEditForm(forms.ModelForm):
    class Meta:
        model = grading
        fields = ['total_score']
     
