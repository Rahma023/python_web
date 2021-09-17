from cal.models import Event
from course.models import Course
from trainers.models import Trainers
from .serializers import CourseSerializer, EventSerializer, StudentSerializer, TrainerSerializer
from rest_framework import viewsets
from student.models import Student

from api import serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainers.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
  
  
