from django import forms
from planner.models import Poi, PoiType, Event, Location
from planner.data_gatherer import DataGatherer
from .widgets import FengyuanChenDatePickerInput
import json


class SearchForm(forms.Form):
    city = forms.CharField(label="Which city would you like to visit?", max_length=80)

    date_from = forms.CharField(
        label="When does your trip start?",
        widget=FengyuanChenDatePickerInput()
    )

    date_to = forms.CharField(
        label="When does your trip end?",
        widget=FengyuanChenDatePickerInput()
    )

    min_budget = forms.IntegerField(
        label="On a scale of 1 to 4, what is your lowest budget level acceptable?",
        min_value=1,
        max_value=4
    )
    @property
    def min_budg(self):
        return int(self.min_budget) + 0

    max_budget = forms.IntegerField(
        label="On a scale of 1 to 4, what is your highest budget level acceptable?",
        min_value=1,
        max_value=4
    )
    @property
    def max_budg(self):
        return int(self.min_budget) + 0

    keywords = forms.CharField(label="What is one keyword that highlights this trip?", max_length=100)

    # ==================================================================================

    def clean_date(self):
        if form.is_valid():
            self.city = form.cleaned_data["city"]
            self.date_from = form.cleaned_data["date_from"]
            self.date_to = form.cleaned_data["date_to"]
            self.min_budget = form.cleaned_data["min_budget"]
            self.max_budget = form.cleaned_data["max_budget"]
            self.keywords = form.cleaned_data["keywords"]


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
            return self.keywords
