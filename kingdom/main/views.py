from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import  Animal

def index(requst):
    animal = Animal.objects.all()
    return render(requst, 'main/index.html', {'animal':animal})

def create(request):
    if request.method == "POST":
        animal = Animal()
        animal.title = Animal.POST.get("title")
        animal.bio = Animal.POST.get("bio")
        animal.firstname = Animal.POST.get("firstname")
        animal.lastname = Animal.POST.get("lastname")
        animal.save()
    return render(request, 'main/create.html')