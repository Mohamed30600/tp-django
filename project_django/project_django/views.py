

from django.shortcuts import render


def helloWorld(request):
    return render(request, "helloWorld.html")


def addition(request):
    if 'num1' in request.GET:
        val1 = int(request.GET['num1'])
    else:
        val1=False
    if 'num2' in request.GET:
        val2 = int(request.GET['num2'])
    else:
        val2=False
        
    result = val1 + val2
    return render(request,"sum.html",{'result':result})