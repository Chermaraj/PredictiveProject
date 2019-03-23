"""Build a multilinear regression model
The goal of this program is to train a MultiLinear Regression Model  on features
that yields the acceptance percentage for the universities with respect to student profiles
"""

# Author: Chermaraj Murugesan <CMQ277@uregina.ca>
# Author: Abhishekkumar Israni <aiv700@uregina.ca>

import pandas as pd
import numpy as np
import itertools
from sklearn.preprocessing import Imputer
from scipy.stats import linregress
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
from PredictiveAcceptance.models import UniversitySampleData

class BuildLinearModel:
#Generic function to fit Multilinear Regression Model for the 
#passed training anf target features

  def build_linear_regression_model(training_features, target_feature):
    model = linear_model.LinearRegression()
    return model.fit(training_features, target_feature)

#Class function to build MultiLinear Regression Model 
#for University Of British Columbia (UBC).Data Analysis for this model is done in Jypter Notebook and 
#observed the independent variables which is highly coefficient with dependent variable
class BuildUBCModel: 

  def build_ubc_model():
    ubc_independent_data = UniversitySampleData.objects.values_list('grescore','undergradcgpa','research_skills').filter(university_code='UBC')
    ubc_dependent_data   = UniversitySampleData.objects.values_list('acceptancepercentage').filter(university_code='UBC')
    training_features    = np.array(list(ubc_independent_data))
    target_feature       = np.array(list(ubc_dependent_data))
    ubc_model            = linear_model.LinearRegression()
    return ubc_model.fit(training_features, target_feature)

#Class function to build MultiLinear Regression Model 
#for University Of Regina(UOR).Data Analysis for this model is done in Jypter Notebook and 
#observed the independent variables which is highly coefficient with dependent variable
class BuildUORModel:

  def build_uor_model():
    uor_independent_data = UniversitySampleData.objects.values_list('undergradcgpa','research_skills').filter(university_code='UBC')
    uor_dependent_data   = UniversitySampleData.objects.values_list('acceptancepercentage').filter(university_code='UOR')
    training_features    = np.array(list(uor_independent_data))
    target_feature       = np.array(list(uor_dependent_data))
    uor_model            = linear_model.LinearRegression()
    return uor_model.fit(training_features, target_feature)


#Class function to build MultiLinear Regression Model 
#for University Of Alberta(UOA).Data Analysis for this model is done in Jypter Notebook and 
#observed the independent variables which is highly coefficient with dependent variable
class BuildUOAModel:

  def build_uoa_model():
    uoa_independent_data = UniversitySampleData.objects.values_list('grescore','undergradcgpa','research_skills').filter(university_code='UBC')
    uoa_dependent_data   = UniversitySampleData.objects.values_list('acceptancepercentage').filter(university_code='UOA')
    training_features    = np.array(list(ubc_independent_data))
    target_feature       = np.array(list(ubc_dependent_data))    
    uoa_model            = linear_model.LinearRegression()
    return uoa_model.fit(training_features, target_feature)



class PredictiveModels:

    def __init__(self):
        self.buildUoRModel = BuildUORModel()
        self.buildUBCModel = BuildUBCModel()
        self.buildUoAModel = BuildUOAModel()

    
    def trainModel(self):
        self.buildUoRModel.build_uor_model()
        self.buildUBCModel.build_ubc_model()
        self.buildUoAModel.build_uoa_model()

PredictiveModels = PredictiveModels()
PredictiveModels.trainModel()    