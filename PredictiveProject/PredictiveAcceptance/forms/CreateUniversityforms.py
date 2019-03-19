from django import forms

from django.forms import ModelForm

from PredictiveAcceptance.models import UniversityNames

class CreateUniversity(forms.ModelForm):
    university_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))

    university_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Name',
                                      'maxlength': '75'}))

    class Meta:
        model = UniversityNames 
        fields = ('university_code', 'university_name')