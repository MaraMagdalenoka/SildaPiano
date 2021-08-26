from django.contrib import admin

# Register your models here.
from .models import LessonPlans
from .models import UserProfile
from .models import *

admin.site.register(LessonPlans)
admin.site.register(UserProfile)
admin.site.register(LessonTimes)

