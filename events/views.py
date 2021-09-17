from django.shortcuts import render
from .forms import School_Events_Form
from .models import Events

# Create your views here.

def register_event(request):
    if request.method=="POST":
        form=School_Events_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=School_Events_Form()
    return render(request,"register_event.html",{"form":form})

def events_list(request):
    events=Events.objects.all()
    return render(request,"events_list.html",{"events":events})

