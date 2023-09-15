from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *

# Create your views here.

def reci(request):
    if request.method == "POST":
        data = request.POST

        receipi_name = data.get('receipi_name')
        receipi_desc = data.get('receipi_desc')
        reci_img = request.FILES.get('reci_img')

        receipi.objects.create(
            receipi_name=receipi_name,
            receipi_desc=receipi_desc,
            reci_img=reci_img
        )
        messages.success(request, "your Receipe has been save ")

        return redirect ('/reci/reci')

    queryset=receipi.objects.all()
    context={'receipi' : queryset}
    return render(request,"reci.html" , context)


def update_reci(request , id):
    queryset = receipi.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        receipi_name = data.get('receipi_name')
        receipi_desc = data.get('receipi_desc')
        reci_img = request.FILES.get('reci_img')

        queryset.receipi_name = receipi_name
        queryset.receipi_desc = receipi_desc

        if reci_img:
            queryset.reci_img = reci_img

        queryset.save()
        
        messages.success(request, "your Receipe has been Updated ")

        return redirect ('/reci/reci')

    context={'receipis' : queryset}

    return render (request, 'update_reci.html', context)
    



def delete_reci(request , id):
    queryset = receipi.objects.get(id = id)
    queryset.delete()
    return redirect ('/reci/reci')


    # id_=int(request.GET['id']) # getting the value of 'id' from
    # # url parameter and converting it into integer using int function
    # # obj=receipi.objects.filter(pk=id_)  # filtering object
    # # with primary key as given in URL paramtere
    # print(id)
    # print("object deleted")   ## printing message to check whether delete is successful or not 