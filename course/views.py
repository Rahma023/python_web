from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course

# Create your views here.

def register_course(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseForm()
    return render(request,"course_register.html", {"form":form})

def course_list(request):
    course=Course.objects.all()
    return render(request,"course_list.html", {"course":course})

def course_update(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_update.html", {"course":course})

def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseForm(request.post,instance=course)
        if form .is_valid():
            form.save
            return redirect("edit_course",id=course.id)
    else:
        form=CourseForm(instance=course)
        return render(request,"edit_course.html", {"form":form})

# def student_list(request):
#     students=Course.objects.all()
#     return render(request,"student_list.html",{"students":students})
