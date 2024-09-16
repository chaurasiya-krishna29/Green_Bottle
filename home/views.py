from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.conf import settings
import random
# Create your views here.

#home
def home(request):
    return render(request,'index.html')
#index
def index_page(request):
    return render(request,"index.html")
#contact
def contact(request):
    if request.method=="POST":
        data=request.POST

        name=data.get('name')    
        email=data.get('email')
        phone=data.get('phone')
        company=data.get('company')
        messages=data.get('messages')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            messages=messages,
        )
    return render(request,"contact.html")

#advertiement
def advertisement(request):
    if request.method=="POST":
        data=request.POST

        first_name=data.get('first-name')
        last_name=data.get('last-name')
        email=data.get('email')
        phone=data.get('phone')
        company_name=data.get('company-name')
        business_type=data.get('business-type')
        advertise=data.get('advertise')
        budget=data.get('budget')
        message=data.get('message')

        Advertise.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            company_name=company_name,
            business_type=business_type,
            advertise=advertise,
            budget=budget,
            message=message

        )
    return render(request,"advertisement.html")




