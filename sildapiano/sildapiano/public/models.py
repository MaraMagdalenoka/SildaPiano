from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField(max_length=110)
    age_above_18 = models.BooleanField(null=True)
    renting = models.BooleanField(null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
