from django.shortcuts import render,redirect
from .models import school
from django.conf import settings
from qrcode import *
from django.db import connection
# Create your views here.

def fetchData(request):

    sql = "SELECT * FROM demo_school"
   
    data = school.objects.raw(sql)
    
    context = {'data': data}

    return render(request,'demo/fetch.html',context)


def home(request):

    data = school.objects.all()

    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        data = name+str(age)
        img  = make(data)
        img_name ='qr'+data+'.png'

        img.save(settings.MEDIA_ROOT + '/qrcode/' + img_name)
        obj = school(name=name,age=age,img_name=img_name)
        obj.save()
        return redirect('demo')
    
    context={
        'data':data
    }
    return render(request,'demo/main.html',context)