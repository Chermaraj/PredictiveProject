from django.shortcuts import render,redirect,render_to_response
from PredictiveAcceptance.filters import UnviersityNamesFilter
from django.http import HttpResponse
from PredictiveAcceptance.forms.SearchUniversityForms import SearchUniversity
from PredictiveAcceptance.models import UniversityNames
from PredictiveAcceptance.models import UniversityNames
from PredictiveAcceptance.models import LookupValues

def searchUniversity(request):
    if request.method == 'GET':

        univ_list = UniversityNames.objects.all();
        country_list = LookupValues.objects.get(lookup_type='COUNTRY')
        univ_code = request.GET['University']
        username = request.session['username']
        if univ_code:           
            universities_list = UniversityNames.objects.filter(university_code=univ_code)
        else:            
            universities_list = UniversityNames.objects.all()      
            
        context = {
               "univ_list": univ_list,
               "country_list":country_list,
               "universities_list": universities_list,
                    } 
        #Unviersity_Filter = UnviersityNamesFilter(request.GET, queryset=universities_list)
        return render(request,'PredictiveAcceptance/HomePage.html',context)

   
def about(request):
    return render(request,
                  "PredictiveAcceptance/about.html",
                     {
            'title'   : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )