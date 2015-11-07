from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db.models import PointField

from cartelisands.models import Cartelisand

class Problem(models.Model):
    place = PointField()
    problem = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    cartelisands = models.ManyToManyField(Cartelisand, blank=True)
