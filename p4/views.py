from django.http import HttpResponse
from django.shortcuts import render

def sample(request):
    return render(request,"sample.html")

def sample1(request):
    return render(request,"directory/sample1.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"King",'name':"Hrushikesh"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange','pineapple']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':19})