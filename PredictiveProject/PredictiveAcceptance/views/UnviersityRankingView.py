from django.shortcuts import HttpResponse, render, redirect
from PredictiveAcceptance.models import UniversityAcceptanceRates,PredictiveUsers

def universityRank(request): 

    #form = universityRankForm(request.POST or None)



  
    # check if the request is post  
    if request.method =='POST':   
  
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        #if form.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database 
  
            # Creating Session with logged in user   
            #request.session['username'] = form.cleaned_data.get('username')
  
            # render it to some another page indicating username was created successfully  
            #return redirect('HomePage')
              
        #else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "PredictiveAcceptance/Login.html", {'form':form})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        username = request.session['username']
        user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
        #form = userLoginForm(None)    
        student_user_id = UniversityAcceptanceRates.objects.filter(student_user_id=user_id)
        #.values_list('student_user_id')
        if not student_user_id.exists():
            context = {
               "message_list": "Please create your profile in system inorder to analyse it",
                    } 

            return render(request, 'PredictiveAcceptance/universityRanking.html',context)

        
        univ_list = UniversityAcceptanceRates.objects.filter(student_user_id=user_id).get()
        context = {
               "univ_list": univ_list,
                    } 
        return render(request, 'PredictiveAcceptance/universityRanking.html',context) 
