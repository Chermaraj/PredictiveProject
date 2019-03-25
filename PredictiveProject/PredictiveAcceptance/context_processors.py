from PredictiveAcceptance.models import PredictiveUsers
def getuserName(request):
   user = PredictiveUsers.objects.get(username=request.session['username'])
   return{'userList': user}
