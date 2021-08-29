from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=110)
    phone_num = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        UserProfile.objects.create(user=instance)


class LessonPlans(models.Model):
    lesson_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    number_of_lessons = models.IntegerField(null=False)
    price_for_all = models.FloatField()


class Lessons(models.Model):
    date = models.DateField(blank=False, null=True)
    hour = models.TimeField(blank=False, null=True)
    available = models.BooleanField(default=True)
    taken_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    paid = models.BooleanField(default=False)

class LessonTimes(models.Model):
    lesson_date = models.DateField()
    lesson_time = models.TimeField()
    lesson_status = models.BooleanField(null=False)