from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render , redirect, get_object_or_404
from PredictiveAcceptance.models import UniversityNames, UniversitySummaries
from PredictiveAcceptance.forms.UniversitySummaryAndInfoForms import UniversityInfoForm, UniversitySummaryForm 
from django.contrib import messages

# Create your views here.

def home(request):
     if request.method == 'POST' :
         form = UniversityInfoForm(request.POST)
         if form.is_valid():
           post = form.save(commit = False)
           post.save()
           #request = 'GET'
           return redirect('/AdminUniversitySummary')
          
     
         else:
           form = UniversityInfoForm()
           context = {'form' : form}
           return render(request,'PredictiveAcceptance/AdminHome.html', context)
     else:
           form = UniversityInfoForm()
           context = {'form' : form}
           return render(request,'PredictiveAcceptance/AdminHome.html', context)

def list(request):
     # form =  UniversitySummaryForm() 
      UniversityObj = UniversitySummaries.objects.all()
      context = {'UniversityObj': UniversityObj }
      return render(request,'PredictiveAcceptance/AdminListOfUniversity.html', context)


    


def summary(request):
     if request.method == 'POST' :
         form = UniversitySummaryForm(request.POST)
         if form.is_valid():
           form.save()
           return redirect('/AdminHome/')
         else: 
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "PredictiveAcceptance/AdminUniversitySummary.html", {'form':form})
          
     else:
           form = UniversitySummaryForm
           context = {'form' : form}
           return render(request,'PredictiveAcceptance/AdminUniversitySummary.html',context)

def editSummary(request,univ_code):
        universities = get_object_or_404(UniversitySummaries ,university_code=univ_code) 
        if request.method == "POST":
            form = UniversitySummaryForm(request.POST or None, instance = universities)
            if form.is_valid():
             form.save()
             return redirect('/AdminHome/')
            
            else:
                  return render(request, "PredictiveAcceptance/AdminUniversitySummary.html", {'form':form})
              
        else:

            form = UniversitySummaryForm(instance = universities)
            
            return render (request, 'PredictiveAcceptance/AdminUniversitySummary.html', {"form":form} )
       