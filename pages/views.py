from django.shortcuts import render

# from django.http import HttpResponse


# def home_page_view(request):
#     return HttpResponse("Hompage")


def home_page_view(request):
    context = {}
    return render(request, "home.html")
