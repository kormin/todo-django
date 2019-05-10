from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200, null=True)


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
