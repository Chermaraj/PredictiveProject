from django.shortcuts import HttpResponse, render, redirect
from PredictiveAcceptance.models import UniversityAcceptanceRates,PredictiveUsers

def acceptanceRate(request,univ_code):

 if request.method =='POST':   
  
  
            return render(request, "PredictiveAcceptance/AcceptanceRate.html", {'form':form})   
 else: 
   
        username = request.session['username']
        user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
        student_user_id = UniversityAcceptanceRates.objects.filter(student_user_id=user_id)
        #.values_list('student_user_id')
        if not student_user_id.exists():
            context = {
               "message_list": "Please create your profile in system inorder to analyse it",
                    } 

            return render(request, 'PredictiveAcceptance/AcceptanceRate.html',context)



        #form = userLoginForm(None)  
        if univ_code == "UOR":  
            univ_list = UniversityAcceptanceRates.objects.values_list('uor_accep_rate').filter(student_user_id=user_id).get()[0]

        if univ_code == "UOA":  
            univ_list = UniversityAcceptanceRates.objects.values_list('uoa_accep_rate').filter(student_user_id=user_id).get()[0]

        if univ_code == "UBC":  
            univ_list = UniversityAcceptanceRates.objects.values_list('ubc_accep_rate').filter(student_user_id=user_id).get()[0]

        context = {
               "univ_list": univ_list,
                    } 
        return render(request, 'PredictiveAcceptance/AcceptanceRate.html',context) 
