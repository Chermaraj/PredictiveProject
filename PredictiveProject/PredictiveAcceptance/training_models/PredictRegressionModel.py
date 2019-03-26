from PredictiveAcceptance.training_models import RegressionModel
from sklearn.linear_model import LinearRegression
from PredictiveAcceptance.models import StudentProfiles
import pandas as pd
import numpy as np

class UORClassfier:

    def predict_uor(self,user_id):
        linearModel = LinearRegression()
        RegModel  = RegressionModel.BuildUORModel()
        linearModel = RegModel.build_uor_model()
        student_data = StudentProfiles.objects.values_list('undergradcgpa','research_skills').filter(user=user_id).get()
        input_data   = np.array(list(student_data)).reshape(1, -1)
        uor_pred = linearModel.predict(input_data)[0]
        return uor_pred
     
class UBCClassfier:  

    def predict_ubc(self,user_id):
        linearModel = LinearRegression()
        RegModel  = RegressionModel.BuildUBCModel()
        linearModel = RegModel.build_ubc_model()
        student_data = StudentProfiles.objects.values_list('grescore','undergradcgpa','research_skills').filter(user=user_id).get()
        input_data   = np.array(list(student_data)).reshape(1, -1)
        ubc_pred = linearModel.predict(input_data)[0]
        return ubc_pred

class UOAClassifier:

       def predict_uoa(self,user_id):
        linearModel = LinearRegression()
        RegModel  = RegressionModel.BuildUOAModel()
        linearModel = RegModel.build_uoa_model()
        student_data = StudentProfiles.objects.values_list('grescore','undergradcgpa','research_skills').filter(user=user_id).get()
        input_data   = np.array(list(student_data)).reshape(1, -1)
        uoa_pred = linearModel.predict(input_data)[0]
        return uoa_pred




class PredictiveModels:

    def __init__(self,user_id=[]):
        self.user_id = user_id
        self.UoRModel = UORClassfier()
        self.UBCModel = UBCClassfier()
        self.UoAModel = UOAClassifier()

    
    def predictRate(self,user_id):
        uor_pred = self.UoRModel.predict_uor(user_id)
        ubc_pred = self.UBCModel.predict_ubc(user_id)
        uoa_pred = self.UoAModel.predict_uoa(user_id)

        return uor_pred,ubc_pred,uoa_pred