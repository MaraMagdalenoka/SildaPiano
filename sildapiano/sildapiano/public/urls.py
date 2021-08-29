from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "public"
urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("", views.lessons_page, name="lessons"),
    path("lessons/contacts/", views.contacts, name="contacts"),
    path("lessons/about/", views.about, name="about"),
    path("lessons/calendar", views.calendar, name="calendar"),
    path("lessons/catalogue", views.catalogue, name="catalogue"),
    path("profile/", views.ProfileView.as_view(template_name="accounts/profile.html"), name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("lessons/payment/", views.payment, name="payment")
]
