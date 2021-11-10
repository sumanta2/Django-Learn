# This file was created by me
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>hello form Home</h1> <br> <a href='https://youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>Django Playlist</a>")


def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Welcome to about Page")

def analyze(request):

    print(request.GET.get('text','This is Default Value')) # it help to get data from formTag get request
    djText=request.GET.get('text','This is Default Value')
    removepunc=request.GET.get('removepunc','off')
    if removepunc =='on':

        analyzed=''
        punctuations='''!(){}[]-;:'"\,<>./?@#$%^&*_~'''
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("Capitalized")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")

