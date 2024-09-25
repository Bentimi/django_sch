from django import forms
from admissionApp.models import admission_approval, aspirants_profile
from django_countries.data import COUNTRIES

class admissionForm(forms.ModelForm):
     gender_options = [
        ("--Gender--", "--Gender--"),
        ("Male", "Male"),
        ("Female", "Female"),
    ]
     next_of_kin_relationship_option = [
        ("--Select an option--", "--Select an option--"),
        ("Brother", "Brother"),
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Sister", "Sister"),
        ("Other", "Other"),
    ]
     first_name = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'First Name',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     middle_name = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'Middle Name',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     last_name = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'Last Name',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     username = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'Username',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     gender = forms.CharField(widget=forms.Select(choices=gender_options,attrs={
            'placeholder':'Gender',
            'class':'form-select shadow-sm rounded-0'
        }), required=False)
     d_o_b = forms.DateField(widget=forms.DateInput(attrs={
         'placeholder':'Date of Birth',
         'class':'form-control shadow-sm rounded-0',
         'type':'date'
     }), required=False)
     phone_no = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'Phone Number',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     email = forms.CharField(widget=forms.NumberInput(attrs={
         'placeholder':'Email',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     address = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Address',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     country = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Country',
            'class':'form-control shadow-sm rounded-0'
        }), required=False)
     state = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'State',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     next_of_kin = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of kin',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     next_of_kin_number = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of Kin Number',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }))
     next_of_kin_email = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of Kin Email',
         'class':'form-control shadow-sm rounded-0',
         'type':'text'
     }), required=False)
     next_of_kin_relationship = forms.CharField(widget=forms.Select(choices=next_of_kin_relationship_option,attrs={
            'placeholder':'Next of Kin Relationship',
            'class':'form-select shadow-sm rounded-0'
        }), required=False)
     passport = forms.ImageField( 
        label="Passport", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }), required=False)
     o_levels = forms.ImageField( 
        label="O'Level Result", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }), required=False)
     utme = forms.ImageField( 
        label="UTME Result", 
        widget=forms.FileInput(
            attrs={
                'type' : 'file',
                'class':"form-control shadow-sm rounded-0", 
                'aria-describedby':"fileHelpId"
                }), required=False)
     password = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Next of Kin Email',
         'class':'form-control shadow-sm rounded-0',
         'type':'password'
     }), required=False)
   
     class Meta:
        model = aspirants_profile
        fields = [
            'first_name', 'middle_name', 'last_name', 'username', 'gender', 'd_o_b', 'phone_no', 'email', 'address', 'country', 'state', 'next_of_kin', 'next_of_kin_number', 'next_of_kin_email', 'next_of_kin_relationship', 'passport', 'o_levels', 'utme', 'password'
        ]
