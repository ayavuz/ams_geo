from django.contrib.gis.db import models
from django.contrib.auth.models import User
# from django.contrib.gis.geos import Point


class GeoLocation(models.Model):
    location = models.PointField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

