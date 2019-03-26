from django import forms
from django.forms import ModelForm
from PredictiveAcceptance.models import PredictiveUsers
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re  

class userRegisterForm(forms.ModelForm):

     username  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter User Name', 
                                      'maxlength': '20', 'pattern':'[A-Za-z ]+',
                                      'required': True}))

     firstname  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter First Name', 'pattern':'[A-Za-z ]+',
                                      'maxlength': '30',
                                      'required': True}))

     middlename  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter Middle Name',
                                      'maxlength': '30'}))

     lastname    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter Last Name', 'pattern':'[A-Za-z ]+',
                                      'maxlength': '20',
                                      'required': True}))

     password    = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'placeholder': 'Password',
                                      'maxlength': '50',
                                      'required': True}))

     email_address  = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                      'placeholder': 'Email Address',
                                      'maxlength': '50',
                                      'required': True}))

     class Meta:
        model = PredictiveUsers 
        fields = ('username', 'firstname', 'middlename', 'lastname', 'password','email_address')


     def clean(self):

           super(userRegisterForm, self).clean

           username   = self.cleaned_data.get('username')
           firstname  = self.cleaned_data.get('firstname')
           middlename = self.cleaned_data.get('middlename')
           lastname   = self.cleaned_data.get('lastname')
           password   = self.cleaned_data.get('password')
           email_address = self.cleaned_data.get('email_address')

           if len(username) < 5:
                    self._errors['username'] = self.error_class(['UserName should be atleast five characters long'])
           
           try:
                validate_username(username)
           except ValidationError as e:
                self._errors['username'] = self.error_class([e])

           if len(firstname) < 4:
                self._errors['firstname'] = self.error_class(['First Name should be atleast four characters long'])

           try:
                validate_email(email_address)
           except ValidationError as e:
                self._errors['email_address'] = self.error_class([e])

           try:
                validate_password(password, self.data,None)
           except ValidationError as e:
                self._errors['password'] = self.error_class([e])
   
           #validate_password(password,None,None )

           return self.cleaned_data

def is_email(string):

    validator = EmailValidator()
    try:
        validator(string)
    except ValidationError:
        return False
    return True 

def validate_email(email_address):
    email = email_address
    if email and PredictiveUsers.objects.filter(email_address=email).count() > 0:
        raise forms.ValidationError(u'This email address is already registered.')
    return email

def validate_username(username):
    userName = username
    if userName and PredictiveUsers.objects.filter(username=userName).count() > 0:
        raise forms.ValidationError(u'This Username is already taken.Pleas try another.')
    return userName



