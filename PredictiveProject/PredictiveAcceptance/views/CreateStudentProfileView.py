from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from PredictiveAcceptance.forms.CreateStudentProfileForms import CreateStudentProfileForm
from PredictiveAcceptance.models import StudentProfiles, PredictiveUsers
from django.contrib import messages
from PredictiveAcceptance.patterns import ObserverPattern

def StudentProfileCreation(request):  
    username = request.session['username']
    form = CreateStudentProfileForm(request.POST or None)
    userList = PredictiveUsers.objects.filter(username=username).get()
    user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
    if (StudentProfiles.objects.filter(user=user_id).exists()):
        userObj = get_object_or_404(StudentProfiles ,user=user_id) 
    else:
        userObj = PredictiveUsers.objects.filter(username=username).get()

    if request.method =='POST':   
  
        if form.is_valid():   
  
            newData = StudentProfiles()
            user_id = PredictiveUsers.objects.values_list('user_id').filter(username=username).get()[0]
            user = PredictiveUsers.objects.get(user_id=user_id)
            newData.user = user
            newData.grescore          = form.cleaned_data.get('grescore')
            newData.englishtest       = form.cleaned_data.get('englishtest')
            newData.undergradcgpa     = form.cleaned_data.get('undergradcgpa')
            newData.workex_months     = form.cleaned_data.get('workex_months')
            newData.research_skills   = form.cleaned_data.get('research_skills')

            newData.save()

            studentProfile = ObserverPattern.studentProfileCore("Profilecore")
            profileObserver = ObserverPattern.ProfileMonitoringCore()

            studentProfile.attach(profileObserver)
            studentProfile.user_id = user_id




            system_messages = messages.get_messages(request)
            for message in system_messages:
             pass
            system_messages.used = True
   
            #messages.success(request, 'Your Profile has been created successfully', extra_tags='alert')
            messages.success(request, 'Your Profile has been saved successfully.You can check the acceptance rate', extra_tags='alert')
              
            #return redirect( "/predictAcceptance/", {'user_id':user_id}) 
            #return render(request, "PredictiveAcceptance/StudentProfileCreation.html", {'form':form ,'userList':userList})   
            
            return render(request, "PredictiveAcceptance/StudentProfileCreation.html", {'form':form ,'userList':userList})

        else:            
            
            return render(request, "PredictiveAcceptance/StudentProfileCreation.html", {'form':form ,'userList':userList})   
    else: 
          
          form = CreateStudentProfileForm(instance = userObj)   
          return render(request, 'PredictiveAcceptance/StudentProfileCreation.html', {'form':form, 'userList':userList}) 
         
           





