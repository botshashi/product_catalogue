from django.db import models
from django.utils import timezone


class User(models.Model):

    class Meta:
        app_label = 'auth_service'

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
