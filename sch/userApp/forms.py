from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userApp.models import Profile

# from userApp.models import 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=30, required=False, help_text='Enter Valid Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class User_update_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Last Name'}),
            'email' : forms.EmailInput(attrs={'type':'email', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Email'}),
        }

class Profile_update_form(forms.ModelForm):
    gender_option = [
        ('-----', '-------'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    marital_status_option = [
        ('------', '------'),
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorce' , 'Divorce'),
        ('Complicated', 'Complicated'),
    ]

    next_of_kin_relationship_option = [
        ('------', '------'),
        ('Mother' , 'Mother'),
        ('Father' , 'Father'),
        ('Brother' , 'Brother'),
        ('Sister' , 'Sister'),
        ('Gaurdian' , 'Gaurdian'),
        ('Others' , 'Others'),
    ]

    profile_passport = forms.ImageField( 
        label="Profile Passport", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-none border-none", 
                'aria-describedby':"fileHelpId"
                }))
    means_of_identity = forms.ImageField(
        required=False, 
        label="Means of identity", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-none border-none", 
                'aria-describedby':"fileHelpId"
                }))
    particulars = forms.ImageField(
        required=False, 
        label="Particulars", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-none border-none", 
                'aria-describedby':"fileHelpId"
                }))
    staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':'form-check-input rounded-0 shadow-none',
        'type':'checkbox'
    }),
    required=False
    )
    class Meta:
        model = Profile
        fields = [
                  'address', 'phone_no', 'd_o_b','marital_status', 
                  'nationality', 'state', 'gender', 'next_of_kin', 'next_of_kin_phone_no', 
                  'next_of_kin_relationship', 'means_of_identity', 'particulars', 'profile_passport', 'staff'
                  ] 

        widgets = {
            'address' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Address'}),
            'phone_no' : forms.NumberInput(attrs={'type' : 'tel', 'class' : 'form-control shadow-none border-1 rounded-0', 'placeholder':'Phone Number'}),
            'd_o_b' : forms.NumberInput(attrs={'type' : 'date', 'class' : 'form-control shadow-none border-1 rounded-0'}),
            'marital_status' : forms.Select(attrs={'class':'form-select shadow-none border-1 rounded-0',}),
            'nationality' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Nationality'}),
            'state' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'State'}),
            'gender' : forms.Select(attrs={'class':'form-select shadow-none border-1 rounded-0',}),
            'next_of_kin' : forms.TextInput(attrs={'type':'text', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Next of Kin'}),
            'next_of_kin_phone_no' : forms.NumberInput(attrs={'type':'tel', 'class':'form-control shadow-none border-1 rounded-0', 'placeholder':'Next of Kin Phone Number'}),
            'next_of_kin_relationship' : forms.Select(attrs={'class':'form-select shadow-none border-1 rounded-0',}),
            'staff' : forms.CheckboxInput(attrs={'type' : 'checkbox', 'class' : 'form-check-input shadow-none border-none'}),
        }