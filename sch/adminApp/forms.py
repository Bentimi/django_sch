from django import forms
from .models import fees_table

class feesRegForm(forms.ModelForm):
    Full_tuition_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Full Tuition',
        'class':'shadow-sm border-1 form-control'
    }), label='Full Tuition')
    part_tuition_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Part Tuition',
        'class':'shadow-sm border-1 form-control'
    }), label='Part Tuition')
    late_reg_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Late Registration',
        'class':'shadow-sm border-1 form-control'
    }), label='Late Registration')
    admission_form_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Admission Form Fee',
        'class':'shadow-sm border-1 form-control'
    }), label='Admission Form Fee')
    acceptance_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Acceptance Fee',
        'class':'shadow-sm border-1 form-control'
    }), label='Acceptance Fee')
    class Meta:
        model = fees_table
        fields = [
            'Full_tuition_fee', 'part_tuition_fee', 'late_reg_fee','admission_form_fee', 'acceptance_fee'
        ]

class edit_tuition(forms.ModelForm):
    Full_tuition_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Full Tuition',
        'class':'shadow-sm border-1 form-control'
    }), label='Full Tuition')
    part_tuition_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Part Tuition',
        'class':'shadow-sm border-1 form-control'
    }), label='Part Tuition')
    class Meta:
        model = fees_table
        fields = [
            'Full_tuition_fee', 'part_tuition_fee'
        ]

class edit_lateReg(forms.ModelForm):
    late_reg_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Late Registration',
        'class':'shadow-sm border-1 form-control'
    }), label='Late Registration')
    late_reg_approval = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':'shadow-sm border-1 form-check-input'
    }),required=False, label='Late Registration Approval')
    class Meta:
        model = fees_table
        fields = ['late_reg_fee', 'late_reg_approval']

class edit_admissionFee(forms.ModelForm):
    admission_form_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Admission Form Fee',
        'class':'shadow-sm border-1 form-control'
    }), label='Admission Form Fee')
    acceptance_fee = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Acceptance Fee',
        'class':'shadow-sm border-1 form-control'
    }), label='Acceptance Fee')
    class Meta:
        model = fees_table
        fields = ['admission_form_fee', 'acceptance_fee']