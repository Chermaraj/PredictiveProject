from django.shortcuts import HttpResponse, render, redirect
from PredictiveAcceptance.forms.UserLoginForms import userLoginForm
from PredictiveAcceptance.models import PredictiveUsers
from PredictiveAcceptance.models import UserTypes
from django.contrib import messages


def userLogin(request): 

    form = userLoginForm(request.POST or None)



  
    # check if the request is post  
    if request.method =='POST':   
  
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if form.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database 
  
            # Creating Session with logged in user   
            request.session['username'] = form.cleaned_data.get('username')
  
            # render it to some another page indicating username was created successfully  
            return redirect('HomePage')
              
        else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "PredictiveAcceptance/Login.html", {'form':form})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        form = userLoginForm(None)    
        return render(request, 'PredictiveAcceptance/Login.html', {'form':form}) 


