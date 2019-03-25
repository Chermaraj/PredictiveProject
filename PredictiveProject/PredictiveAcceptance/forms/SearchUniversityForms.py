
from django import forms

from django.forms import ModelForm

from PredictiveAcceptance.models import UniversityNames

class SearchUniversity(forms.ModelForm):
    university_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter University Code',
                                      'maxlength': '75'}))
    
    university_name = forms.ModelMultipleChoiceField(
    label='List',
    required=False,
    queryset=UniversityNames.objects.all(),
    widget= forms.SelectMultiple(attrs={'class': 'input-field second-wrap'}))


    class Meta:
        model = UniversityNames 
        fields = ('university_code', 'university_name')