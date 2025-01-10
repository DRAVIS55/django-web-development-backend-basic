from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import  Feature,Item


# Create your views here.
def home(request):
    listt=Feature.objects.all()
    return render(request,'index.html', {'list':listt} )

def service(request):
    services=Item.objects.all()
    return render(request,'service-details.html',{'listt':services})


def login(request):
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        # Getting the form data from the request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2==password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is arleady in use !')
                return redirect('home')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'the username is in use chhose a unique username')
                return redirect('home')
            else:
                messages.success(request,'submitted successfully!')
                user=User.objects.create_user(username=username,email=email,password=password2)
                user.save()
                return redirect(request,'login')
        else:
            messages.info(request,'password does not match')
            return redirect('home')
    else:
        return render(request,'register.html')







