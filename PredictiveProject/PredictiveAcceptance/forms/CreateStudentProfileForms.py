from django import forms
from django.forms import ModelForm
from PredictiveAcceptance.models import PredictiveUsers
from PredictiveAcceptance.models import StudentProfiles


class CreateStudentProfile(forms.ModelForm):

    grescore = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))


    englishtest =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))
    undergradcgpa =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))
    workex_months =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))
    research_skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))

