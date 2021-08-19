from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username =
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age_above_18 = models.BooleanField()
    renting = models.BooleanField()
    description = models.CharField(max_length=1000)