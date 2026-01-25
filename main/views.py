from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
            message = form.cleanet_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['k.m19981102@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject,message,sender,recipients)
            return HttpResponseRedirect('thank_you.html')    
    else:
        form = ContactForm()    
    return render(request,'contact.html',{'form':form})

def project(request,id) :
    project = get_object_or_404(Project, pk=id)
    return render(request,'project.html',{'project':project})