from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
#avjeet.
def index(request):
    context = {
        'variable': "this is sent"
    }
    messages.success(request,"this is a test massage")
    return render(request,'index.html', context)

def about(request):
    return render(request,"about.html")
    # return HttpResponse('this is about page')


def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, contact=contact, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent')
        
    return render(request,"contact.html")
