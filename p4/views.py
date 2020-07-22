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

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,ab):
    a = ab.split(" ")
    sum = int(a[0]) + int(a[1])
    return HttpResponse(str(sum))

def ab(request,a,b):
    sum = int(a) + int(b)
    return HttpResponse(str(sum))

def abc(request,a,b,c):
    sum = int(a) + int(b) + int(c)
    return HttpResponse(str(sum))

def great(request,a,b):
    if(a > b):
        return HttpResponse("<h1> a = {} is greater</h1>".format(a))
    else:
        return HttpResponse("<h1> b = {} is greater</h1>".format(b))

def string19(request,name):
    
    k = "aeiouAEIOU"
    vowels = ""
    constants = ""
    for h in name:
        if h in k:
            vowels += h
            
        else:
            constants += h
    return render(request,"directory/vowels.html",{'string':name,'vowels':vowels,'constants':constants}) 
    