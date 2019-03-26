"""
Definition of urls for PredictiveProject.
"""

from django.conf.urls import include,url
from django.urls import path,re_path
from PredictiveAcceptance.views import CreateUniversityView,SearchUniversityView,HomePageView,UserRegisterView,UserLoginView,UnviersityRankingView,CreateStudentProfileView,PredictAcceptRateView,AcceptanceRateView
#Django processess URL patterns in the order they appear in array 

urlpatterns = [
    url(r'^create_university$',CreateUniversityView.create_university, name='create_university'),
    url(r'^about$',CreateUniversityView.about, name='about'),
    url(r'^contact',CreateUniversityView.contact, name='contact'),
    url(r'^searchUniversity/$', SearchUniversityView.searchUniversity, name='searchUniversity'),    
    url(r'^HomePage/$', HomePageView.HomePage, name='HomePage'),
    url(r'^userRegister/$', UserRegisterView.userRegister, name='userRegister'),    
    url(r'^$', UserLoginView.userLogin, name='userLogin'),       
    url(r'^userLogOut/$', UserLoginView.userLogOut, name='userLogOut'),         
    url(r'^universityRank/$', UnviersityRankingView.universityRank, name='universityRank'),    
    url(r'^StudentProfileCreation/$', CreateStudentProfileView.StudentProfileCreation, name='StudentProfileCreation'),
    url(r'^predictAcceptance/$', PredictAcceptRateView.predictAcceptance, name='predictAcceptance'),   
    path(r'^acceptanceRate/<str:univ_code>/$',AcceptanceRateView.acceptanceRate, name='acceptanceRate'),
    ]