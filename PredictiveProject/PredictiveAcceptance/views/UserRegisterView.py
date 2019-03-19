from django.shortcuts import HttpResponse, render, redirect 
from PredictiveAcceptance.forms.UserRegisterForms import userRegisterForm
from PredictiveAcceptance.models import PredictiveUsers
from django.contrib import messages


def userRegister(request): 

    form = userRegisterForm(request.POST or None)

  
    # check if the request is post  
    if request.method =='POST':   
  
        # Pass the form data to the form class 
        #etails = userRegisterForm(request.POST) 
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if form.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database    
            post = form.save(commit = False) 
  
            # Finally write the changes into database 
            post.save()   
            messages.success(request, 'The Username has been  registered successfully!', extra_tags='alert')
  
            # render it to some another page indicating username was created successfully  
            form = userRegisterForm(None)
            return render(request,"PredictiveAcceptance/UserRegister.html", {'form':form})
              
        else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "PredictiveAcceptance/UserRegister.html", {'form':form})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        form = userRegisterForm(None)    
        return render(request, 'PredictiveAcceptance/UserRegister.html', {'form':form}) 

