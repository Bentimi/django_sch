from django import forms
from paymentApp.models import invoice_table


class Payment_form(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
            'placeholder': 'Card Number',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='Card Number', required=True)
    cvv = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
            'placeholder': 'cvv',
            'class':'form-control shadow-sm border-1',
            'type' : 'text'
        }), label='CVV', required=True)
    expire_date = forms.CharField(widget=forms.TextInput(attrs={
             'placeholder': 'mm/yy',
            'class':'form-control shadow-sm border-1',
            # 'type' : 'datetime'
        }), label='Expiry Date', required=True)
    
class tuitionForm(forms.Form):
    trans_type = [
        ("--Select Option--", "--Select Option--"),
        ("Part Payment", "Part Payment"),
        ("Full Payment", "Full Payment"),
    ]
    transaction_type = forms.CharField(max_length=16, widget=forms.Select(choices=trans_type, attrs={
            'class':'form-select shadow-sm border-1'
        }), required=False, label='Payment Category')
    