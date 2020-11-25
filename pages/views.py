import random
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView, RedirectView,TemplateView
from .models import *
from .forms import ContactInfoForm
import json
import requests
from services.models import Service
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def home(request):
#     return render(request,'index.html')

# class Company(ListView):
#     model = CompanyHeader
#     context_object_name = 'company'
#     template_name = 'index.html'

def Company(request):
    details=CompanyHeader.objects.all()
    data=Service.objects.all()

    return render(request,'index.html', {'detail':details,'service':data})

# def Contact(request):
#     details=CompanyHeader.objects.all()


#     return render(request,'contact.html', {'detail':details})


def Contact(request):
    details=CompanyHeader.objects.all()
    data=Service.objects.all()

    success = False
    if request.method == 'POST':
        fm = ContactInfoForm(request.POST)
        message1 = request.POST['name']
        message2 = request.POST['email']
        message3 = request.POST['phone']
        message4 = request.POST['subject']
        message5 = request.POST['message']

        message = "Name: " + message1 + "\n" + "Email: " + message2 + "\n"  +"Phone: " + message3 + "\n" + "Subject : " + message4 + "\n" + "Message : " + message5

    #Recaptcha Key     
        clientkey = request.POST['g-recaptcha-response']
        secretkey= '6LeTjOgZAAAAANybFF_oU-V83QiJ7rllo13-zb59'
        capthchaData={
        'secret': secretkey,
        'response': clientkey

        }
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
        response=json.loads(r.text)
        verify=response['success']
        print('The success :', verify)
            
        if verify:
            
            if fm.is_valid():        
                fm.save()
                # emp1.run()  # calling run function from models.py
                send_mail(
                'Contact Query',
                message,
                settings.EMAIL_HOST_USER,
                ['biratrai1111@gmail.com'],
                fail_silently=False,
                )
                messages.add_message(request, messages.INFO, 'Thank you for your message')
                success = True
                fm = ContactInfoForm()

        else:
            messages.add_message(request, messages.INFO, 'Please complete the Captcha')



    else:

        fm = ContactInfoForm()
    return render(request, 'contact.html', {'form': fm, 'success': success, 'detail': details, 'service':data})


