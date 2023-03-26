from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import mimetypes
import os
from .forms import Contact
from .models import contact_lead
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        fm = Contact(request.POST)
        if fm.is_valid():
            nm =  fm.cleaned_data['name']
            ph_no = fm.cleaned_data['phone_number']
            email = fm.cleaned_data['email_id']
            msg = fm.cleaned_data['msg']
            con = contact_lead(name=nm,email_id=email,phone_number = ph_no,msg=msg)
            con.save()  
            messages.success(request, 'Contact request submitted successfully.')
            mail(request,email)
            
            return HttpResponseRedirect('/')  
        else:
            messages.error(request, 'Invalid form submission.')         
    else:
        fm = Contact()
        return render(request,'index.html',{'form':fm})

def contact(request):
    if request.method == 'POST':
        fm = Contact(request.POST)
        if fm.is_valid():
            nm =  fm.cleaned_data['name']
            ph_no = fm.cleaned_data['phone_number']
            email = fm.cleaned_data['email_id']
            msg = fm.cleaned_data['msg']
            print(nm,ph_no,email,msg)
            con = contact_lead(name=nm,email_id=email,phone_number = ph_no,msg=msg)
            con.save()    
            messages.success(request, 'Contact request submitted successfully.')         
            mail(request,email)
            
            return HttpResponseRedirect('/')  
        else:
            messages.error(request, 'Invalid form submission.')      
    else:
        fm = Contact()
    return render(request,'contact.html',{'form':fm})


def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')


def mail(request,email_id):
    msg_obj = contact_lead.objects.filter(email_id = email_id).values()
    for i in range(len(msg_obj)):
        name = msg_obj[i].get('name')
        phone_number = msg_obj[i].get('phone_number')
        email = msg_obj[i].get('email_id')
        mesg = msg_obj[i].get('msg')
    subject = "New Enquiry is recieved"
    msg = f'Hi, A new enquiry is recieved with the following details :\n Message : {mesg},\n name: {name},\n Phone number : {phone_number},\n Email id : {email}'
    to = ["nishant.kumar164@gmail.com"]
    email_from = settings.EMAIL_HOST_USER
    res = send_mail(subject,msg,email_from,to) 
    if res ==1:
        msg = "mail send" 
        print("passed")
    else:
        msg ="mail not send"
        print("failed")
    return HttpResponse(msg)   

         