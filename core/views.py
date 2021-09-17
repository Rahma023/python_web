from course.models import Course
from events.models import Events
from trainers.models import Trainers
from student.models import Student
from django.shortcuts import render
from student.models import Student
from trainers.models import Trainers
from course.models import Course
from events.models import Events

# Create your views here.

def home(request):
    students=Student.objects.count()
    trainers=Trainers.objects.count()
    course=Course.objects.count()
    events=Events.objects.count()
    data={"students":students, "trainers":trainers, "course":course, "events":events}
    return render(request,"home.html",data)

