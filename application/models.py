from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=100)
    url = models.URLField()
