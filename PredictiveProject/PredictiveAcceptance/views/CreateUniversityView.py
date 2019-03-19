from django.shortcuts import render
from django.http import HttpResponse
from PredictiveAcceptance.forms.CreateUniversityforms import CreateUniversity

def create_university (request):
    """Renders the basic  create operation."""
    if request.method == 'GET':

        # Get  form to display
        form = CreateUniversity(request.GET)
        return render(request, 'PredictiveAcceptance/index.html',
                      {'form': form,
                       'title': "Create University"})

    data = dict()
    if request.method == 'POST':
        # Get the form data
        form = CreateUniversity(request.POST)

        if form.is_valid():
            form.save()  # insert new row

            # Return some json response back to the user
            data = """ Your data has been inserted successfully, thank you! """

        else:

            # Extract form.errors
            data = 'Error'

        return HttpResponse(data)

def about(request):
    return render(request,
                  "PredictiveAcceptance/about.html",
                     {
            'title'   : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )