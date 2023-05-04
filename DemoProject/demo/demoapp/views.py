from tempfile import template

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import student
from django.template import loader

# Create your views here.

def index(request):
    d=student.objects.all().values()
    return render(request,"index.html",{"data":d})



def add(request):
    return render(request,"add.html")



def addrecord(request):
    a= request.POST['first']
    b= request.POST['last']
    c=request.POST['contact']
    d=request.POST['address']
    stud = student(firstname=a, lastname=b)
    stud.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  stud = student.objects.get(id=id)
  stud.delete()
  return HttpResponseRedirect(reverse('index'))




def addrecord(request):
    a=request.POST['first']
    b=request.POST['last']
    c= request.POST['contact']
    d=request.POST['address']
    stud=student(firstname=a,lastname=b,contact=c,address=d)
    stud.save()

    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    stud=student.objects.get(id=id)
    context={
        'mymember':stud
    }
    return render(request,"update.html",context)

def updaterecord(request,id):
    a=request.POST['first']
    b = request.POST['last']
    c = request.POST['contact']
    d = request.POST['address']
    stud=student.objects.get(id=id)
    stud.firstname=a
    stud.lastname=b
    stud.contact=c
    stud.address=d
    stud.save()
    return HttpResponseRedirect(reverse('index'))
