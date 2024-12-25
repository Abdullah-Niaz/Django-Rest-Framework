from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
