from django.shortcuts import render
from PredictiveAcceptance.filters import UnviersityNamesFilter
from django.http import HttpResponse
from PredictiveAcceptance.forms.SearchUniversityForms import SearchUniversity
from PredictiveAcceptance.models import UniversityNames

def searchUniversity (request):
    if request.method == 'GET':

        # Get  form to display
        form = SearchUniversity(request.GET)
        universities_list = UniversityNames.objects.all()
        Unviersity_Filter = UnviersityNamesFilter(request.GET, queryset=universities_list)
        return redirect('HomePage',{'form': form })

   
def about(request):
    return render(request,
                  "PredictiveAcceptance/about.html",
                     {
            'title'   : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )