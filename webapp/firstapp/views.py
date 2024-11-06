from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def firstview(request):
    print(request.method)
    if request.method == 'GET':
        res_obj=render(request,'first.html')
        return res_obj
    if request.method == 'POST':
    
       v1=int(request.POST['t1'])
       v2=int(request.POST['t2'])
       res=v1+v2
       #print(request.post)
       #return HttpResponse('addition of given number is'+str(res))
       return render(request,'first.html',{'request':res})                

def secondview(request):
    return HttpResponse('we are learning django')