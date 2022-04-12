from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import  Animal
from .forms import AnimalForm
from django.views.generic import DetailView, UpdateView, DeleteView

def index(requst):
    animal = Animal.objects.all()
    return render(requst, 'main/index.html', {'animal':animal})

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "main/detail.html"
    context_object_name =  'animal'


class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = "main/create.html"
    form_class = AnimalForm

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = '/'
    template_name = "main/delete.html"


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