# This file was created by me
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>hello form Home</h1> <br> <a href='https://youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>Django Playlist</a>")


def index(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("Welcome to about Page")

def removepunch(request):
    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse("Capitalized")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")

