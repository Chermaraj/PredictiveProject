from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from PredictiveAcceptance.models import PredictiveUsers
from django.template import RequestContext
from PredictiveAcceptance.forms.SearchUniversityForms import SearchUniversity
from PredictiveAcceptance.models import UniversityNames
from PredictiveAcceptance.models import LookupValues


def HomePage(request): 

    #form = userLoginForm(request.POST or None)
           
    # check if the request is post  
    if request.method =='POST':   
  
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        #if form.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database 
  
            # Creatinbg Session with logged in user   
            request.session['username'] = form.username
  
            # render it to some another page indicating username was created successfully  
            #return redirect(request,"PredictiveAcceptance/HomePage.html")
              
        #else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            #return render(request, "PredictiveAcceptance/Login.html", {'form':form})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        username = request.session['username']
        univ_list = UniversityNames.objects.all();
        country_list = LookupValues.objects.get(lookup_type='COUNTRY')
        form = SearchUniversity(request.GET)
        context = {
        "univ_list": univ_list,
        "country_list":country_list,
        "form" : form
             } 

        return render(request, 'PredictiveAcceptance/HomePage.html', context) 