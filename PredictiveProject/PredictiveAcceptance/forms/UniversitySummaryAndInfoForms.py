"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from PredictiveAcceptance.models import UniversityNames, UniversitySummaries
from django.core.validators import MaxValueValidator, MinValueValidator


class UniversityInfoForm(forms.ModelForm):
          
             
                university_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter University Code',                                
                                           'required': True, 
                                           }),
                                           min_length=3, max_length=10)

                university_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter University Name',                                 
                                           'required': True}),
                                            min_length = 5 , max_length= 20)
                
                class Meta:
                   model = UniversityNames
                   fields = ('university_code','university_name')

class UniversitySummaryForm(forms.ModelForm):

                             
              university_code = forms.ModelChoiceField(queryset = UniversityNames.objects.all(),
                                                       empty_label = "Select University Code",
                                                       required = True)

              avg_grescore  = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '3',
                                       'required': True}),
                                       ) 
              avg_eng_score    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                      'step': '0.5', 'min':'1.0', 'max':'9.0',
                                                              
                                      'required': True}))
              avg_undergradcgpa  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                      'step': '0.01', 'min':'1.00', 'max':'10.00',
                                                                
                                      'required': True}))
              avg_workex_months  = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                      'maxlength': '2',                               
                                      'required': True}), validators=[MaxValueValidator(30), MinValueValidator(1)])
              avg_research_skills  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                      'step': '1', 'min':'10', 'max':'100',
                                                                       
                                      'required': True}))
              avg_acceptancepercentage  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       
                                      'required': True}))
              
               
    
              class Meta:
               model = UniversitySummaries
               fields = ('university_code','avg_grescore','avg_eng_score','avg_undergradcgpa','avg_workex_months','avg_research_skills','avg_acceptancepercentage')


              def clean(self):

               super(UniversitySummaryForm, self).clean

               university_code   = self.cleaned_data.get('university_code')
               avg_grescore      = self.cleaned_data.get('avg_grescore')
               avg_eng_score   = self.cleaned_data.get('avg_eng_score')
               avg_undergradcgpa   = self.cleaned_data.get('avg_undergradcgpa')
               avg_workex_months = self.cleaned_data.get('avg_workex_months')
               avg_research_skills = self.cleaned_data.get('avg_research_skills')
               avg_acceptancepercentage = self.cleaned_data.get('avg_acceptancepercentage')

               
               if avg_grescore > 340:
                    self._errors['avg_grescore'] = self.error_class(['Average GRE Score should be less than or equal to 340'])
           
              
               if avg_grescore < 265:
                    self._errors['avg_grescore'] = self.error_class(['Avg GRE Score cannot be less than 265'])
               
               
           
               return self.cleaned_data

            
