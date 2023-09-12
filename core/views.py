from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import AddApplicationForm
from .models import Application

@login_required
def home(request):
    return render(request,'home.html')


def login_user(request):
    if request.method == "POST":
        us = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=us,password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "You are Successfully logged in !")
            return redirect('home')
        else:
            messages.error(request, "You have failed to login try again !")
            return redirect('login')
    return render(request,'login.html')





def application_form(request):
    form = AddApplicationForm()
    if request.method=="POST":
        form = AddApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email_id = form.cleaned_data['email_id']
            contact = form.cleaned_data['contact_number']
            application = Application.objects.filter(email_id=email_id, contact_number=contact)[0]
            return render (request, 'applicationform.html', {'app_id':application.application_id})
    else:
        return render(request, 'applicationform.html',{'form':form, 'app_id':''})
    return render(request, 'applicationform.html',{'form':form, 'app_id':''})



def apply(request):
    return render(request, 'apply.html')


def status(request):
    if request.method == "POST":
        app_id = request.POST['application_id']

        try:
            application = Application.objects.get(application_id=app_id)
            object_exist = True
            return render(request, 'application_status.html', {'appid':app_id, 'application':application, 'object_exist':object_exist})
        except:
            # application = None
            # object_exist = False
            messages.error(request, "No Application Found. Enter application id again !")
            return redirect('status')
        # return render(request, 'application_status.html', {'appid':app_id, 'application':application, 'object_exist':object_exist})
    return render(request, 'application_status.html')


@login_required
def startup_applications(request):
    applications = Application.objects.filter(isAccepted = False, isRejected = False)
    query = request.GET.get('query','')
    filter = request.GET.get('filter')
    if filter == 'accepted':
        applications = Application.objects.filter(isAccepted=True)
    elif filter == 'rejected':
        applications = Application.objects.filter(isRejected=True)
    
    if query:
        applications = Application.objects.filter(Q(application_id__icontains=query) | Q(startup_name__icontains=query))
    
    return render(request, 'startupApplications.html', {'applications':applications, 'query':query, 'filter':filter})


@login_required
def application_review(request, application_id):
    try:
        application = Application.objects.get(application_id=application_id)

    except:
        messages.error(request,"No Application has been found")
        return redirect('startup_applications')
    return render(request, 'applicationReview.html',{'application':application})