"""
Definition of urls for PredictiveProject.
"""

from django.conf.urls import include,url
from django.urls import path,re_path
from PredictiveAcceptance.views import AdminSiteViews,CreateUniversityView,SearchUniversityView,HomePageView,UserRegisterView,UserLoginView,UnviersityRankingView,CreateStudentProfileView,PredictAcceptRateView,AcceptanceRateView,UniversityInfoView
#Django processess URL patterns in the order they appear in array 

urlpatterns = [
    url(r'^about$',CreateUniversityView.about, name='about'),
    url(r'^contact',CreateUniversityView.contact, name='contact'),
    url(r'^searchUniversity/$', SearchUniversityView.searchUniversity, name='searchUniversity'),    
    url(r'^HomePage/$', HomePageView.HomePage, name='HomePage'),
    url(r'^userRegister/$', UserRegisterView.userRegister, name='userRegister'),    
    url(r'^$', UserLoginView.userLogin, name='userLogin'), 
    url(r'^userLogin/$', UserLoginView.userLogin, name='userLogin'), 
    url(r'^userLogOut/$', UserLoginView.userLogOut, name='userLogOut'),         
    url(r'^universityRank/$', UnviersityRankingView.universityRank, name='universityRank'),    
    url(r'^StudentProfileCreation/$', CreateStudentProfileView.StudentProfileCreation, name='StudentProfileCreation'),
    url(r'^predictAcceptance/$', PredictAcceptRateView.predictAcceptance, name='predictAcceptance'), 
    url(r'^viewUniversityInfo/$', UniversityInfoView.viewUniversityInfo, name='viewUniversityInfo'),
    path(r'^acceptanceRate/<str:univ_code>/$',AcceptanceRateView.acceptanceRate, name='acceptanceRate'),
    #Following are the AdminSiteURLS
    url(r'^AdminHome/$', AdminSiteViews.home, name='home'),
    path(r'^AdminListOfUniversity/$', AdminSiteViews.list, name='list'),    
    path(r'^AdminUniversitySummary/$', AdminSiteViews.summary, name='summary'),
    path(r'^AdminUniversitySummary/(?:[-\w]+)?(?:/([-\w]+/))?$', AdminSiteViews.summary, name='summary'),
    path(r'^AdminUniversitySummary/<str:univ_code>/$', AdminSiteViews.editSummary, name='editSummary'),
    ]