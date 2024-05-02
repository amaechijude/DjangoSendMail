from django.shortcuts import render, redirect

from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

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
            
            print(f"{email}\n{subject}\n{body}\n")

            send_mail(
                subject,
                body,
                email,
                ['amaechijude178@gmail.com'],
            )
            messages.info(request, "Form submited")
            return redirect('index')

        messages.info(request, "Form not valid")
        return redirect('index')
    
    form = ContactForm()
    return render(request, 'index.html', {"form": form})