from django.db import models
import uuid

# Create your models here.

# ========================================================

class SearchReq(models.Model):
    city = models.CharField(max_length=80)
    date_from = models.DateField()
    date_to = models.DateField()
    min_budget = models.IntegerField()
    max_budget = models.IntegerField()
    keywords = models.CharField(max_length=100) 

# Poi stands for place of interest
class Poi(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    PRICE_CHOICES = [
        (0, 'unknown price level'),
        (1, '$'),
        (2, '$$'),
        (3, '$$$'),
        (4, '$$$$'),
    ]
    priceLV = models.IntegerField(
        choices=PRICE_CHOICES,
        default=0,
        verbose_name="price level",
    )
    rating = models.DecimalField(max_digits=2, decimal_places=1,)
    ratingCount = models.IntegerField()
    placeType = models.ForeignKey(
        'PoiType',
        on_delete=models.SET_DEFAULT,
        default='other types',
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_DEFAULT,
        default='unknown',
    )
    
    class Meta:
        ordering = ['rating', 'ratingCount']
    # --------------------
    def __str__(self):
        return self.name
    

# PoiType right now can only be three types:
# 0) others
# 1) restaurant
# 2) hotel
class PoiType(models.Model):
    pType = models.CharField(
        max_length=80,
        default='unknown',
    )
    # --------------------
    def __str__(self):
        return self.pType


# interesting local events that a person can check out
class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    title = models.CharField(max_length=150)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    starting_time = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )
    venue_name = models.CharField(max_length=80)
    url_link = models.TextField()
    venue_url_link = models.TextField()
    # --------------------
    def __str__(self):
        return self.title


# location refers to the city and the country
# right now we'll just work with Canada
class Location(models.Model):
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    # --------------------
    def __str__(self):
        return f"{self.city}, {self.country}"
