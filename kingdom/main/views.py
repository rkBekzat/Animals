from django.shortcuts import render

def index(requst):
    return render(requst, 'main/index.html')