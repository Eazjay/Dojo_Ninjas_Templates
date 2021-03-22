from django.shortcuts import render, redirect
from .models import *

def index(request):
    request.session['count'] = 0
    context = {
        "count": request.session['count'],
        "all_dojos": Dojo.objects.all(),
    }
    return render(request, 'dojo.html', context)

def processDojoForm(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def processNinjaForm(request):
    dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo)
    return redirect('/')

def deleteInstance(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')