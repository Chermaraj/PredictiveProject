from django.shortcuts import render, redirect
from django.template import RequestContext
from PredictiveAcceptance.models import UniversitySummaries


def viewUniversityInfo(request):
      UniversityObj = UniversitySummaries.objects.all()
      context = {'UniversityObj': UniversityObj }
      return render(request,'PredictiveAcceptance/ViewUniversityInfo.html', context)
