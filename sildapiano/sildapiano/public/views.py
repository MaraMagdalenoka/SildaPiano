from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


def homepage(request):
    return render(request, "./homepage.html")


def lessons_page(request):
    return render(request, "./lessons_page.html")


def contacts(request):
    return render(request, "./contacts.html")


def about(request):
    return render(request, "./about.html")


def calendar(request):
    lessons_time = LessonTimes.objects.all()
    return render(request, "./calendar.html", {"lessons_time": lessons_time})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"


def catalogue(request):
    lessons_info = LessonPlans.objects.all()
    return render(request, "./catalogue.html", {"lessons_info": lessons_info})

