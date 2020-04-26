# I havve created this file
from django.http import HttpResponse 
from django.shortcuts import render



def index(request):
    params = {'name':'harry', 'place': 'Mars'}
    return render(request, 'index.html', params)
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text', 'default')#Get the text
    removepunc = request.POST.get('removepunc', 'off')#check values
    fullcaps = request.POST.get('fullcaps', 'off')#check values
    newlines = request.POST.get('newlines', 'off')#check values
    extraspaceremover = request.POST.get('extraspaceremover', 'off')#check values
    #check which check box is on:
    if removepunc == "on":
        punctuations = '''~`!@#$%^&*()|\?/,.:;"'<>'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlines == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove the exrra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

        
        
    else:
        return HttpResponse("error")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def newlineremove(request):
#     return HttpResponse('''newlineremove<a href="/">back</a>''')

# def spaceremove(request):
#     return HttpResponse("spaceremover")

# def charcount(request):
#     return HttpResponse("character counter")