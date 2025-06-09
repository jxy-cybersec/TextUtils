# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>Harry</h1>")

# def about(request):
#     return HttpResponse("about jxy")
# Code for video 5
# from django.http import HttpResponse
# def jxy(request):
#     with open ('one.txt', 'r') as f:
#         content = f.read()
#     return HttpResponse(content)

# code for video 6
# from django.http import HttpResponse
# def yt(request):
#     return HttpResponse('<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry</a>')


# Code for video 7
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Home <br><a href='removepunc'>removepunc</a> <br><a href='capitalizefirst'>capfirst</a> <br><a href='newlineremove'>newlineremove</a> <br><a href='spaceremove'>spaceremove</a> <br><a href='charcount'>charcount</a>")

# def removepunc(request):
#     return HttpResponse("remove punc <br><a href='/'>back</a>")

# def capfirst(request):
#     return HttpResponse("capitalize first <br><a href='/'>back</a>")

# def newlineremove(request):
#     return HttpResponse("Newline remove <br><a href='/'>back</a>")

# def spaceremove(request):
#     return HttpResponse("space remove <br><a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("char count <br><a href='/'>back</a>")


# Code for video 8
from django.http import HttpResponse
from django.shortcuts import render
