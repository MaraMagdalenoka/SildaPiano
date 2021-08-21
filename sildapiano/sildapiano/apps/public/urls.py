from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lessons/", views.lessons_page, name="lessons"),
    path("lessons/contacts/", views.contacts, name="contacts"),
    path("lessons/about/", views.about, name="about"),
    path("lessons/calendar", views.calendar, name="calendar")
]
