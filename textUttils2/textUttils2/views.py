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

    djText=request.POST.get('text','This is Default Value')
    removepunc=request.POST.get('removepunc','off')
    fullCaps=request.POST.get('fullCaps','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    spaceRemover=request.POST.get('spaceRemover','off')
    CharCount=request.POST.get('CharCount','off')

    params={'purpose':'Error','analyzed_text':'!!No Option Selected'}
    
    if removepunc =='on':
        analyze=''
        punctuations='''!(){}[]-;:'"\,<>./?@#$%^&*_~'''
        for char in djText:
            if char not in punctuations:
                analyze=analyze+char
        djText=analyze
        # params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    if fullCaps=='on':
        analyze=''
        for char in djText:
            analyze=analyze+char.upper()
        djText=analyze
        # params={'purpose':'Full Capitalize','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    if newLineRemover=='on':
        analyze=''
        for char in djText:
            if char not in "\n" and  char not in "\r":    #'\n' and '\r' used to identify nextLine character(generate pressing Enter key)
                analyze=analyze+char
        djText=analyze
        # params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    if spaceRemover=='on':
        analyze=''
        for index,char in enumerate(djText):   #enumerate() method return index value as well as string
            if not(djText[index]  in ' ' and djText[index+1]  in ' '):
                analyze=analyze+char
        djText=analyze
        # params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    if CharCount=='on':
        length=len(djText)
        length="\nYour input String's Length is:{}".format(length)
        djText=djText+length
        # params={'purpose':'Remove New Line', 'analyzed_text':length}
        # return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    if(removepunc!= 'on' and fullCaps!= 'on' and newLineRemover!= 'on' and spaceRemover!= 'on' and CharCount!= 'on'):
        return(HttpResponse("Error"))
        
    params={'purpose':'Multiple Operation','analyzed_text':djText}
    return render(request,'analyze.html',params)  #here send analyze.html template as a responce
    

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

