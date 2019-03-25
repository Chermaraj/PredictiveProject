 from django import forms
from django.forms import ModelForm
from PredictiveAcceptance.models import PredictiveUsers
from PredictiveAcceptance.models  import UserTypes
from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validators
from django.core.exceptions import EmptyResultSet
import re 
import bcrypt

class userLoginForm(forms.ModelForm):

     username  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter User Name', 
                                      'maxlength': '20',
                                      'required': True}))

     password    = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'placeholder': 'Password',
                                      'maxlength': '50',
                                      'required': True}))

     userType    = forms.ModelChoiceField(queryset= UserTypes.objects.all(),
                                          empty_label="Select User Type",
                                          required=True )




   
     class Meta:
        model = PredictiveUsers 
        fields = ('username', 'password')


     def clean(self):

           super(userLoginForm, self).clean

           username   = self.cleaned_data.get('username')
           password   = self.cleaned_data.get('password')
           userType   = self.cleaned_data.get('userType')

           try:
                validate_userExists(username)
           except ValidationError as e:
                self._errors['username'] = self.error_class([e])

           try:
                validate_userPassword(username,password)
           except ValidationError as e:
                self._errors['password'] = self.error_class([e])

           try:
                validate_userType(username,userType)
           except ValidationError as e:
                self._errors['userType'] = self.error_class([e])

           return self.cleaned_data

def validate_userPassword(username,password):
 
   if PredictiveUsers.objects.filter(username=username).exists():   
     user = PredictiveUsers.objects.filter(username=username).first()
     if not (bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))):
       raise forms.ValidationError(u'Invalid password.')
   return password

def validate_userExists(username):
    userName = username

    if not(PredictiveUsers.objects.filter(username=userName).exists()):
       raise forms.ValidationError(u'No user found.Please register')
    return userName
 
def validate_userType(username,userType):
    user = UserTypes.objects.filter(user_type=userType).first()

    if not(PredictiveUsers.objects.filter(username=username,user_type_id=user.user_type_id).exists()):
         raise forms.ValidationError(u'Invalid User Type')
    return userType





