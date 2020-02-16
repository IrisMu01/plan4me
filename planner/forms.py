from django import forms
from planner.models import Poi, PoiType, Event, Location
from planner.data_gatherer import DataGatherer
import json


class SearchForm(forms.Form):
    city = forms.CharField(max_length=80)
    date_from = str(forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M']))
    date_to = str(forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M']))
    min_budget = forms.IntegerField(min_value=1, max_value=4)
    max_budget = forms.IntegerField(min_value=1, max_value=4)
    keywords = forms.CharField(max_length=100)
    @property
    def min_budg(self):
        return self.min_budget + 0
    @property
    def max_budg(self):
        return self.min_budget + 0

    def __str__(self):
        return f"{self.city}:\n from {self.date_from} to {self.date_to},\n budget range = {self.min_budget} ~ {self.max_budget},\n keywords = {self.keywords}\n"

    def makeAPICall(self):
        if self.is_valid():
            DataGatherer.get_location_data(self.city, self.min_budg(), self.max_budg(), "restaurant")
            DataGatherer.get_location_data(self.city, self.min_budg(), self.max_budg(), "lodging")
            DataGatherer.get_event_data(self.city, self.date_from, self.date_to, self.keywords)
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