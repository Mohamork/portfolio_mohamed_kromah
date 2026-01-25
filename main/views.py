from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Project,Tag
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.
def home(request) :
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request,'home.html',{'projects':projects,'tags':tags})

def contact(request) :
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['k.m19981102@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject,message,sender,recipients)
            messages.success(request,'Your request was submitted successfully')
            return HttpResponseRedirect('thank-you')    
    else:
        form = ContactForm()    
    return render(request,'contact.html',{'form':form})

def thank_you(request):
    storage = messages.get_messages(request)
    if not any(msg.level == messages.SUCCESS for msg in storage):
        return HttpResponseRedirect('/contact/')
    return render(request,'thank_you.html')

def project(request,id) :
    project = get_object_or_404(Project, pk=id)
    return render(request,'project.html',{'project':project})