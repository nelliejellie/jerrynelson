from django.shortcuts import render
from .models import Portfolio,Services

# Create your views here.

def index(request):
    myservices = Services.objects.all()
    myportfolio = Portfolio.objects.all()
    context ={
        'myservices': myservices,
        'myportfolio': myportfolio,
    }
    return render(request, 'index.html', context)
