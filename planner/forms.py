from django import forms
from planner.models import Poi, PoiType, Event, Location
from planner.data_gatherer import DataGatherer
import json

class SearchForm(forms.Form):
    city = forms.CharField(label="city", max_length=80)
    date_from = forms.DateField(label="date_from")
    date_to = forms.DateField(label="date_to")
    min_budget = forms.IntegerField(min_value=1, max_value=4)
    max_budget = forms.IntegerField(min_value=1, max_value=4)
    keywords = forms.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}:\n from {self.date_from} to {self.date_to},\n budget range = {self.min_budget} ~ {self.max_budget},\n keywords = {self.keywords}\n"

    def makeAPICall(self):
        if self.is_valid():
            DataGatherer.get_location_data(self.city, min_budget, max_budget, "restaurant")
            DataGatherer.get_location_data(self.city, min_budget, max_budget, "lodging")
            DataGatherer.get_event_data(self.city, date_from, date_to, keywords)
            try:
                with open("restaurant_data.json", "r") as read_file:
                    json.load(read_file)
                with open("hotel_data.json", "r") as read_file:
                    json.load(read_file)
                with open("eventful_data.json", "r") as read_file:
                    json.load(read_file)
            except:
                return "one of the API calls weren't successful:\n no json file created as a result of the search"
        else:
            return f"is_valid() returned False for {self}"