from django.shortcuts import HttpResponse, render, redirect
from PredictiveAcceptance.forms.CreateStudentProfileForms import CreateStudentProfileForm
from PredictiveAcceptance.models import StudentProfiles, PredictiveUsers
from django.contrib import messages

def StudentProfileCreation(request):  
    username = request.session['username']
    form = CreateStudentProfileForm(request.POST or None)
    userList = PredictiveUsers.objects.filter(username=username).get()
  
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
   
            messages.success(request, 'Your Profile has been created successfully', extra_tags='alert')
  
            return redirect('/StudentProfileCreation/')
        else:            
            
            return render(request, "PredictiveAcceptance/StudentProfileCreation.html", {'form':form ,'userList':userList})   
    else: 
          
          form = CreateStudentProfileForm(None)   
          return render(request, 'PredictiveAcceptance/StudentProfileCreation.html', {'form':form, 'userList':userList}) 
         
           





