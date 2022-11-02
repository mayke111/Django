from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Page")


def artikel(request, year):
    year = year
    str = year
    return HttpResponse(year)
