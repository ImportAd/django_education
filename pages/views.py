from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Hompage")


def about_page_view(request):
    return render(request, "pages/about.html")
