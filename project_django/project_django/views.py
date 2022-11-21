

from django.shortcuts import render


def helloWorld(request):
    return render(request, "helloWorld.html")


def addition(request):
    result=0
    
   
    val1=(request.GET.get("num1", 0))
    val2=(request.GET.get("num2", 0))
    val11=int(val1)
    val22=int(val2)
        
    result =val11+val22
    return render(request,"sum.html",{'result':result})