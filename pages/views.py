from django.shortcuts import render,redirect
from .models import Portfolio,Services,Contact
from django.contrib import messages,auth

# Create your views here.

def index(request):
    myservices = Services.objects.all()
    myportfolio = Portfolio.objects.all()
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['message-subject']
        body = request.POST['body']
        form = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, body=body)
        form.save()
        messages.success(request, 'your message has been sent successfully')
        return redirect('index')
        
    context ={
        'myservices': myservices,
        'myportfolio': myportfolio,
    }
    return render(request, 'index.html', context)
