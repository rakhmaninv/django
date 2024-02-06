from django.shortcuts import render
from .models import Person
from django.http import HttpResponse


def index(request):
    return render(request, 'finalapp/index.html')


def about(request):
    return render(request, 'finalapp/about.html')


def contacts(request):
    contacts = Person.objects.all()
    return render(request, 'finalapp/contacts.html',  {'contacts': contacts})
