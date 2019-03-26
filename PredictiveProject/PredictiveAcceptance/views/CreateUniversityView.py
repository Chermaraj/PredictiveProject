from django.shortcuts import render
from django.http import HttpResponse
from PredictiveAcceptance.forms.CreateUniversityforms import CreateUniversity


def about(request):
    return render(request,
                  "PredictiveAcceptance/about.html",
                     {
            'title'   : "About PredSys"
        }
    )


def contact(request):
    return render(request,
                  "PredictiveAcceptance/contact.html",
                     {
            'title'   : "Contact PredSys"
        }
    )