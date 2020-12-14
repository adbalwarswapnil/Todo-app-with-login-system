from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You have successfully logged in.')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username/password')
            return redirect('/')
    else:
        return render(request, 'login.html')

@csrf_exempt 
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('/')
            else:
                
                #user = get_user_model().objects.create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                sendConfirm(user)
                #user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                #user.save();
                redirect('/')
        else:
            messages.info(request,'Password do not match')
            return redirect('/')
        messages.info(request,'You have successfully registered your account. Please check your email for confirmation.')
        return redirect('/')

    else:
        return render(request, 'register.html')

@csrf_exempt 
def logout(request):
    messages.info(request,'Successfully logged out.')
    auth.logout(request)
    return redirect('/')