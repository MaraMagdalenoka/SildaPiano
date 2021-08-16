from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, './homepage.html')

def lessons_page(request):
    return render(request, './lessons_page.html')

def contacts(request):
    return render(request, './contacts.html')

def about(request):
    return render(request, './about.html')
