from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from planner.models import Poi, PoiType, Event, Location, SearchReq
from planner.forms import SearchForm
import json
# Create your views here.

# homepage is an absolutely static page
def index(Request):
    context = {}
    return render(Request, 'core/homepg.html', context=context)

def search(Request):
    if Request.method == 'POST':
        # if it's a POST request,
        # which means that the user has filled out the form (hopefully properly)
        form = SearchForm(Request.POST)
        if form.is_valid():
            # print('form is valid.')
            # ↑ for debugging only

            # more code here to:
            # 1. clean the data
            form.clean_data()
            # 2. make the API call
            '''
            print(form.city, type(form.city))
            print(form.date_from, type(form.date_from))
            print(form.date_to, type(form.date_to))
            print(form.min_budget, type(form.min_budget))
            print(form.max_budget, type(form.max_budget))
            print(form.keywords, type(form.keywords))
            ↑ for debugging purposes
            '''
            form.makeAPICall()
            # We don't make the API call for now; too slow and could cost us google account $$$ 


            return HttpResponseRedirect('result/')
            # redirects the user to the result page
        else:
            print('invalid form.')
            print(form.errors)
            print(Request.POST)
            # will see these in the terminal for debugging
    else:
        form = SearchForm()
        # if it's a GET request intead of a POST one,
        # generates an empty form for the user to fill out
    return render(Request, 'core/search.html', {'form': form})

def search_and_display(Request):
    context = {}
    '''
    with open("json_data/restaurant_data.json", "r") as read_file:
        json.load(read_file)
    with open("json_data/lodging_data.json", "r") as read_file:
        json.load(read_file)
    with open("json_data/eventful_data.json", "r") as read_file:
        json.load(read_file)
    '''
    return render(Request, 'core/result.html', context=context)

