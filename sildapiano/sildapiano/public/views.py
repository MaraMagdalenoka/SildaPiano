from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sildapiano.public.forms import SignUpForm
from .models import *


def homepage(request):
    return render(request, "./homepage.html")


def lessons_page(request):
    return render(request, "./lessons_page.html")


def contacts(request):
    return render(request, "./contacts.html")


def about(request):
    return render(request, "./about.html")


# def calendar(request):
#     return render(request, "./calendar.html")


def calendar(request):
    lessons = Lessons.objects.all()
    return render(request, "./calendar.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"


def catalogue(request):
    lessons_info = LessonPlans.objects.all()
    return render(request, "./catalogue.html", {"lessons_info": lessons_info})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone_num = form.cleaned_data.get('phone_num')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.description = form.cleaned_data.get('description')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, "./lessons_page.html")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
