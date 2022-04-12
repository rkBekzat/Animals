from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import  Animal
from .forms import AnimalForm


def index(requst):
    animal = Animal.objects.all()
    return render(requst, 'main/index.html', {'animal':animal})

def create(request):
    error = ''
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Wrong format"

    form = AnimalForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/create.html', data)