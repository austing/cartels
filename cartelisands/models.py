from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField

class Cartelisand(models.Model):
    user = models.OneToOneField(User)
    most_recent_place = PointField(blank=True, null=True)
