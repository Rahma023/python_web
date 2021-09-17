
from trainers.models import Trainers
from django.shortcuts import render, redirect
from .forms import TrainersFillingForm
from django import forms

# Create your views here.

def register_trainers(request):
    if request.method=="POST":
        form=TrainersFillingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainersFillingForm()
    return render(request,"register_trainers.html",{"form":form})

def trainers_list(request):
    trainers=Trainers.objects.all()
    return render(request,"trainers_list.html",{"trainers":trainers})

def trainers_profile(request,id):
    trainers=Trainers.objects.get(id=id)
    return render(request,"trainers_profile.html",{"trainers":trainers})

def edit_trainers(request,id):
    trainers=Trainers.objects.get(id=id)
    if request.method=="POST":
        form=TrainersFillingForm(request.POST,instance=trainers)
        if form.is_valid():
            form.save()
        return redirect("trainers_profile", id=trainers.id)
    else:
        form=TrainersFillingForm(instance=trainers)
        return render(request,"edit_trainers.html", {"form":form})
