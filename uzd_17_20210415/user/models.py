from django.db import models


class User(models.Model):

    name = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
