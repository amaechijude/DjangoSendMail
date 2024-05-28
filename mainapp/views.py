from django.shortcuts import render, redirect

from .forms import * #ContactForm, SignupForm, Lo
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings
import time
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth import authenticate, login, logout
# Create your views here.
#from allauth.account.views import login
#from allauth.socialaccount.views import ConnectionsView

def index(request, recipient_username):
    if request.user.is_authenticated:
        context = {
            'recipient_username': recipient_username,
        }
        return render(request, 'index.html', context)
    return redirect('login_user')

#def room(request, room_name):
 #   return render(request, 'room.html', {"room_name": room_name})

def room(request, recipient_username):
    if request.user.is_authenticated:
        recipient_username = request.user.username
        context = {
            'recipient_username': recipient_username,

        }
        return render(request, 'room.html', context)
    return redirect('login_user')
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        messages.info(request, 'Error')
        return redirect('signup')
    form = SignupForm()
    return render(request, 'signup.html', {"form":form,})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
        
            if user != None:
                login(request, user)
                messages.info(request, 'You are logged in')
                return redirect('index')
            else:
                messages.info(request, 'Profile not found')
                return redirect('login_user')
    form = LoginForm()
    return render(request, 'login.html', {"form":form})

#log out   
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login_user')
    return redirect('login_user')


"""

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            body = f"Message from: {name}\n{message}"
            email_from = settings.EMAIL_HOST_USER
            print(f"{email}\n{subject}\n{body}\n")
            time.sleep(5)
            try:
                send_mail(
                    subject,
                    body,
                    email_from,
                    [email],
                    #fail_silently=False
                )
            
                messages.info(request, "Form submited")
                return redirect('index')
            except TimeoutError:
                messages.info(request, "TimeoutError")
                return redirect('index')
                

        messages.info(request, "Form not valid")
        return redirect('index')
    
    form = ContactForm()
    return render(request, 'index.html', {"form": form})

"""