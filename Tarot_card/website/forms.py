from django import forms
from django.forms import widgets
from .models import contact_lead
from django.core import validators


class Contact (forms.ModelForm):
    class Meta:
        model = contact_lead
        fields = ['name','phone_number','email_id','msg']
        # labels = {'name':'Enter full name', 'phone_number': 'Phone number', 'Email_id': 'Email Id', 'msg': 'Message'}
        error_messages = {'name':{'required':'Please Enter your full name'},
                          'phone_number':{'required':'enter your correct phone number', 'min_lenght':'please enter 10 digit correct number'} ,
                          'email_id':{'required': 'enter correct email id'}}
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'contactus', 'placeholder':'Full Name'}),
            'phone_number':forms.TextInput(attrs={'class':'contactus', 'placeholder': 'Phone Number'}),
            'email_id':forms.EmailInput(attrs={'class':'contactus', 'placeholder': 'Email'}),
            'msg':forms.Textarea(attrs={'class':'contactus', 'placeholder': 'Message'}),
            
        }
        
        



