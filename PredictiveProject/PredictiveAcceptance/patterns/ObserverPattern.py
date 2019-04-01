from PredictiveAcceptance.training_models import PredictRegressionModel
from PredictiveAcceptance.models import StudentProfiles, PredictiveUsers, UniversityAcceptanceRates


class studentProfileCore:
        def __init__(self, user_id):
                self._observers = []
                self.user_id = user_id
 
        def attach(self, observer):
                if observer not in self._observers: 
                        self._observers.append(observer)

        def detach(self, observer):
                try:
                        self._observers.remove(observer)
                except ValueError:
                        print("Observer is already not in the list of observers.")

        def notify(self):
                for observer in self._observers: 
                        observer.predict(self)
                 
        @property
        def user_id(self):
                '''The @property decorator makes a property object 'user_id', on which a setter can be defined, as done below.'''
                return self._user_id
 
        #Setter that sets the temperature of core
        @user_id.setter
        def user_id(self, user_id):
                '''Notify the observers whenever student changes the profile details.
                   @user_id.setter notation signifies the setter method of the user_id property which
                   allows to call the learnig model using the assignment operator'''
                self._user_id= user_id
                self.notify()
                 
class ProfileMonitoringCore:

  def predict(self, subject):
   studentId = subject._user_id
   predictRate = PredictRegressionModel.PredictiveModels()
   uor_pred,ubc_pred,uoa_pred = predictRate.predictRate(studentId)

   newData = UniversityAcceptanceRates()
   student_user = PredictiveUsers.objects.get(user_id=studentId)
   newData.student_user = student_user
   newData.uor_accep_rate = uor_pred
   newData.uoa_accep_rate = ubc_pred
   newData.ubc_accep_rate = uoa_pred
   newData.save()
