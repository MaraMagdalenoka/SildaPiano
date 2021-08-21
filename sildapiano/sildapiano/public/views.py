from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def homepage(request):
    return render(request, "./homepage.html")


def lessons_page(request):
    return render(request, "./lessons_page.html")


def contacts(request):
    return render(request, "./contacts.html")


def about(request):
    return render(request, "./about.html")


def calendar(request):
    return render(request, "./calendar.html")


def catalogue(request):
    return render(request, "./catalogue.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"