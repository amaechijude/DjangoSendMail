from django.shortcuts import render, redirect

from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings
import time

# Create your views here.


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