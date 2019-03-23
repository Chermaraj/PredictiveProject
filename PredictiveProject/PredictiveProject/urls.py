"""
Definition of urls for PredictiveProject.
"""

from django.conf.urls import include,url
from django.urls import path,re_path
from PredictiveAcceptance.views import CreateUniversityView,SearchUniversityView,HomePageView,UserRegisterView,UserLoginView
#Django processess URL patterns in the order they appear in array 
urlpatterns = [
    url(r'^$',CreateUniversityView.create_university, name='create_university'),
    url(r'^create_university$',CreateUniversityView.create_university, name='create_university'),
    url(r'^about$',CreateUniversityView.about, name='about'),
    url(r'^searchUniversity/$', SearchUniversityView.searchUniversity, name='searchUniversity'),    
    url(r'^HomePage/$', HomePageView.HomePage, name='HomePage'),
    url(r'^userRegister/$', UserRegisterView.userRegister, name='userRegister'),    
    url(r'^userLogin/$', UserLoginView.userLogin, name='userLogin'),
    ]