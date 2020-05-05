from django.db import models

# from django.contrib.auth.models import User

class User(models.Model):
    phoneno1 = models.CharField(max_length=11, blank=True)
# Create your models here.


