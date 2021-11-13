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

def contact(request):
    return HttpResponse("Welcome to Contact Page")

def analyze(request):

    print(request.GET.get('text','This is Default Value')) # it help to get data from formTag get request
    djText=request.GET.get('text','This is Default Value')
    removepunc=request.GET.get('removepunc','off')
    fullCaps=request.GET.get('fullCaps','off')
    newLineRemover=request.GET.get('newLineRemover','off')
    spaceRemover=request.GET.get('spaceRemover','off')
    CharCount=request.GET.get('CharCount','off')
    

    analyzed=''
    if removepunc =='on':

        punctuations='''!(){}[]-;:'"\,<>./?@#$%^&*_~'''
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    elif fullCaps=='on':
        analyzed=djText.upper()
        params={'purpose':'Full Capitalize','analyzed_text':analyzed}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    elif newLineRemover=='on':
        for char in djText:
            if char not in '/n':
                analyzed=analyzed+char
        params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    elif spaceRemover=='on':
        for index,char in enumerate(djText):   #enumerate() method return index value as well as string
            if not(djText[index]  in ' ' and djText[index+1]  in ' '):
                analyzed=analyzed+char
        params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    elif CharCount=='on':
        length=len(djText)
        length="Your input String's Length is:{}".format(length)
        params={'purpose':'Remove New Line', 'analyzed_text':length}
        return render(request,'analyze.html',params)  #here send analyze.html template as a responce

    else:
        return HttpResponse("Error")

def navbar(request):   #This create for practice purpose not for Textutils
    return HttpResponse('''
       <a href='https://www.youtube.com'>Youtube</a> <a href='https://www.google.com'>Google</a>
        
    ''')
# def capfirst(request):
#     return HttpResponse("Capitalized")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")

