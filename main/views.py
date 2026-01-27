from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Project,Tag
from django.core.mail import EmailMessage
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
            
            recipients = [settings.CONTACT_EMAIL]
            if cc_myself:
                recipients.append(sender)

            email= EmailMessage(
                subject=subject,
                body=f'Portfolio form submission from {sender}\n\n {message}',
                from_email = settings.EMAIL_HOST_USER,
                to = recipients,
                reply_to= [sender],
            )
            email.send(fail_silently=False)
            
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