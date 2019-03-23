from PredictiveAcceptance.models import PredictiveUsers
def getuserName(request):
   user = PredictiveUsers.objects.get(username=request.session['username'])
   print(user)
   return{'userList': user ,'testme': 'Hello world!'}
