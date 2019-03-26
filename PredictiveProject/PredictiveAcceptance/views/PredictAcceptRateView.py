from PredictiveAcceptance.training_models import PredictRegressionModel
from django.shortcuts import render
from django.http import HttpResponse
from PredictiveAcceptance.forms.CreateStudentProfileForms import CreateStudentProfileForm
from PredictiveAcceptance.models import StudentProfiles, PredictiveUsers, UniversityAcceptanceRates
from django.contrib import messages

def predictAcceptance(request):

     if request.method == 'GET':

         username = request.session['username']
         user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
         predictRate = PredictRegressionModel.PredictiveModels()
         uor_pred,ubc_pred,uoa_pred = predictRate.predictRate(user_id)

         newData = UniversityAcceptanceRates()
         user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
         student_user = PredictiveUsers.objects.get(user_id=user_id)
         newData.student_user = student_user
         newData.uor_accep_rate = uor_pred
         newData.uoa_accep_rate = ubc_pred
         newData.ubc_accep_rate = uoa_pred
         newData.save()
         system_messages = messages.get_messages(request)
         for message in system_messages:
           pass
         system_messages.used = True

         #messages.success(request, 'Your Profile has been saved successfully.You can check the acceptance rate', extra_tags='alert')

         form = CreateStudentProfileForm(None) 
         return render(request, "PredictiveAcceptance/StudentProfileCreation.html", {'form':form})  


