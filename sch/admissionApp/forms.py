from django import forms
from .models import User
from admissionApp.models import admission_approval, aspirants_profile
from userApp.models import Profile, users_status
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class registrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Username')
    email = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class':'form-control shadow-sm border-1',
            'type' : 'email'
        }), label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password',
        'class':'form-control shadow-sm border-1',
        'type' : 'password'
        }), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm password',
        'class':'form-control shadow-sm',
        'type' : 'password'
        }), label='Confirm Password')
    class Meta:
        model = User
        fields = [
            'id','first_name', 'last_name', 'username', 'email', 'password1', 'password2'
        ]

class confirmationForm(forms.ModelForm):
    aspirant = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':'form-check-input shadow-sm',
        'type':'checkbox'
    }), label='I agreed with terms and conditions')
    class Meta:
        model = users_status
        fields = ['aspirant']

class edit_userForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='First Name', disabled=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Last Name', disabled=True)
    email = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class':'form-control shadow-sm border-1',
            'type' : 'email'
        }), label='Email', disabled=True)
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email'
        ]

class loginForm(AuthenticationForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Username',
        'class' : 'form-control shadow-sm border-1',
        'type':'text'
    }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder':'Password',
        'class':'form-control shadow-sm border-1',
        'type':'password'
    }))
    class Meta:
        model = User
        fields = [
            'username', 'password'
        ]

class reg_profileForm(forms.ModelForm):
    marital_status_options = [
         ("--Select an Option--", "--Select an Option--"),
         ("Single", "Single"),
         ("Married", "Married"),
         ("Others", "Others"),
     ]
    gender_options = [
         ("--Select an Option--", "--Select an Option--"),
         ("Male", "Male"),
         ("Female", "Female"),
     ]
    next_of_kin_relationship_option = [
        ("--Select an Option--", "--Select an Option--"),
        ("Brother", "Brother"),
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Sister", "Sister"),
        ("Other", "Other"),
    ]
    d_o_b = forms.DateField(widget=forms.DateInput(attrs={
        'class' : 'form-control shadow-sm border-1',
        'type':'date'
    }))
    other_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Other Name',
        'class':'form-control shadow-sm border-1',
        'type' : 'text'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',
        'class':'form-control shadow-sm border-1',
        'type' : 'text'
    }))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class':'form-control shadow-sm border-1',
        'type' : 'text'
    }))
    marital_status = forms.CharField(widget=forms.Select(choices=marital_status_options,attrs={
            'class':'form-select shadow-sm border-1'
        }))
    gender = forms.CharField(widget=forms.Select(choices=gender_options,attrs={
            'class':'form-select shadow-sm border-1'
        }))
    next_of_kin = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Next of kin',
        'class':'form-control shadow-sm border-1',
        'type' : 'text'
    }))
    next_of_kin_phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Next of kin phone number',
        'class':'form-control shadow-sm border-1',
        'type' : 'text'
    }))
    next_of_kin_relationship = forms.CharField(widget=forms.Select(choices=next_of_kin_relationship_option,attrs={
            'class':'form-select shadow-sm border-1'
        }))
    class Meta:
        model = Profile
        fields = [
             'other_name','address', 'phone_no', 'd_o_b','marital_status','gender', 'next_of_kin', 'next_of_kin_phone_no', 'next_of_kin_relationship'
        ]

class profile_registrationForm(forms.ModelForm):
    d_o_b = forms.DateField(widget=forms.DateInput(attrs={
        'class' : 'form-control shadow-sm border-1',
        'type':'date'
    }))
    other_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Other Name',
        'class':'form-control shadow-sm rounded-0',
        'type' : 'text'
    }))
    class Meta:
        model = Profile
        fields = [
            'other_name','address', 'phone_no', 'd_o_b','marital_status', 
            'nationality', 'state', 'gender', 'next_of_kin', 'next_of_kin_phone_no', 
            'next_of_kin_relationship',
        ]

class admissionForm(forms.ModelForm):
     
     course_options = [
        ("--Select Course--", "--Select Course--"),
        ("Digital Marketing", "Digital Marketing"),
        ("Business World", "Business World"),
        ("Media Technology", "Media Technology"),
        ("Communications", "Communications"),
        ("Business Ethics", "Business Ethics"),
    ]
     sponsorhip_options = [
         ("--Select an Option--", "--Select an Option--"),
         ("Parents", "Parents"),
         ("Guardian", "Guardian"),
         ("Others", "Others"),
     ]

     sponsorhip = forms.CharField(widget=forms.Select(choices=sponsorhip_options,attrs={
            'placeholder':'Sponsor',
            'class':'form-select shadow-sm rounded-0'
        }))
     country = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Country',
            'class':'form-control shadow-sm rounded-0'
        }))
     state = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'State',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }))
     course = forms.CharField(widget=forms.Select(choices=course_options,attrs={
            'placeholder':'Course',
            'class':'form-select shadow-sm rounded-0'
        }))
     next_of_kin_address = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of Kin Address',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }))
     next_of_kin_email = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of Kin Email',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }))
     passport = forms.ImageField( 
        label="Passport", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }))
     o_levels = forms.ImageField( 
        label="O'Level Result", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }))
     utme = forms.ImageField( 
        label="UTME Result", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }))
     national_identity = forms.ImageField( 
        label="National Identity Card", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }))
   
     class Meta:
        model = aspirants_profile
        fields = [
            'sponsorhip', 'country', 'state', 'course', 'next_of_kin_email', 'next_of_kin_address', 'passport', 'o_levels', 'utme', 'national_identity'
        ]