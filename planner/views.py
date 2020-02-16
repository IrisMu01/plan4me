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
            print(Request.POST)
    else:
        form = SearchForm()
    return render(Request, 'core/search.html', {'form': form})

def search_and_display(Request):
    context = {}
    return render(Request, 'core/result.html', context=context)

