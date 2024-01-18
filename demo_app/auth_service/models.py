from django.db import models

# Create your models here.


class User(models.Model):

    class Meta:
        db_table = 'user'
        app_label = 'demo_app'

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
