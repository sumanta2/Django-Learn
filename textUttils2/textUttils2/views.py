# This file was created by me
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hello form HomePage</h1>")

def about(request):
    return HttpResponse("Welcome to about Page")