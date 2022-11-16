

from django.shortcuts import render


def helloWorld(request):
    return render(request,"helloWorld.html")


def addition(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2
    return render(request,"sum.html",{'result':result})