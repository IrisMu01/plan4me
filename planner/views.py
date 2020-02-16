from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from planner.models import Poi, PoiType, Event, Location, SearchReq
from planner.forms import SearchForm
# Create your views here.

# homepage is an absolutely static page
def index(Request):
    context = {}
    return render(Request, 'core/homepg.html', context=context)

def search(Request):
    if Request.method == 'POST':
        form = SearchForm(Request.POST)
        if form.is_valid():
            print('form is valid.')
            result = forms.makeAPICall()
            print(result)
            return HttpResponseRedirect('/thanks/')
        else:
            print('invalid form.')
            print(form.errors)
            print(type(Request.POST.__getitem__('date_to')))
    else:
        form = SearchForm()
    return render(Request, 'core/search.html', {'form': form})

def search_and_display(Request):
    # first, check if the request is a POST request
    if Request.method == 'POST':
        # create a form instance and populate it
        # with the data from the request:
        # this process is called BINDING THE DATA TO THE FORM
        form = SearchForm(Request.POST)
        print(Request.POST.values)
        # check whether it's a valid form
        if form.is_valid():
            # if True is returned from is_valid(),
            # the populated values will be stored into
            # form.cleaned_data (yep the form defined above)
            print('form is valid.')
            result = form.makeAPICall()
            print(result)
            return HttpResponseRedirect('/thanks/')# return to a new URL
        else:
            print('invalid form.')
    else:
        form = SearchForm()
    return render(Request, 'core/result.html', {'form': form})

