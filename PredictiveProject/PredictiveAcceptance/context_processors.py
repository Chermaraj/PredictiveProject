from PredictiveAcceptance.models import PredictiveUsers
def getuserName(request):
   if(request.session['username']):
      user = PredictiveUsers.objects.get(username=request.session['username'])
      return{'userList': user}
   else:
       user = ['NoEmptyList']
       return{'userList': user}
