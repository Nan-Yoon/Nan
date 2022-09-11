from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import studentModel


def index (request):
        return HttpResponse("Hello This is view")

def home(request):
        template = loader.get_template('myfirst.html')
        return HttpResponse(template.render())

def second(request):
        template = loader.get_template('mysecond.html')
        return HttpResponse(template.render())

def student(request):
        mystudent = studentModel.objects.all().values()
        output = ""
        for x in mystudent:
                output += x["name"]
        return HttpResponse(output)

def add(request):
        template = loader.get_template('addstudent.html')
        return HttpResponse(template.render({}, request))

def addrecord(request):
        x = request.POST['roll']
        y = request.POST['name']
        mystudent = studentModel(roll=x, name=y)
        mystudent.save()
        return HttpResponseRedirect(reverse('student'))

def showstudent(request):
        mystudent = studentModel.objects.all().values()
        template = loader.get_template('showstudent.html')
        context = { 'mystudent': mystudent,}
        return HttpResponse(template.render(context, request))



