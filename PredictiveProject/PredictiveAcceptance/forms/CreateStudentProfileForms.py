from django import forms
from django.forms import ModelForm
from PredictiveAcceptance.models import PredictiveUsers
from PredictiveAcceptance.models import StudentProfiles


class CreateStudentProfileForm(forms.ModelForm):

      grescore      = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control GreWidth',
                                       'maxlength': '3','min':'260', 'max':'340',
                                       'required': True}),
                                       ) 

      englishtest    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control engWidth',
                                      'step': '0.5', 'min':'1.0', 'max':'9.0',                       
                                      'required': True}))

      undergradcgpa  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control CGPAWidth',
                                      'step': '0.01', 'min':'1.00', 'max':'10.00',                       
                                      'required': True}))

      workex_months  = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control WorkExWidth',
                                      'maxlength': '2', 
                                      'required': True}))


      research_skills  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control SkillWidth',
                                      'step': '1', 'min':'10', 'max':'100',                                 
                                      'required': True}))
      class Meta:
        model = StudentProfiles 
        fields = ('grescore','englishtest','undergradcgpa','workex_months','research_skills')

      def clean(self):

           super(CreateStudentProfileForm, self).clean

           grescore          = self.cleaned_data.get('grescore')
           englishtest       = self.cleaned_data.get('englishtest')
           undergradcgpa     = self.cleaned_data.get('undergradcgpa')
           workex_months     = self.cleaned_data.get('workex_months')
           research_skills   = self.cleaned_data.get('research_skills')

   

           return self.cleaned_data


