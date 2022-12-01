from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    price = models.IntegerField(default=None)
    description = models.TextField(default=None)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=None)


class Category(models.Model):
    name = models.CharField(max_length=100)
