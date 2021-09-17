from django.db import models
from rest_framework import fields, serializers
from student.models import Student
from trainers.models import Trainers
from course.models import Course
from cal.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age","date_of_birth","roll_number","student_email","nationality","student_id","id_number","gender","phone_number","county","profile","medical_report","date_of_enrollment","language")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainers
        fields=("first_name","last_name","age","date_hired","email_address","nationality","national_id","gender","phone_number","county","profile","qualification","occupation","date_hired","contract","language")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name","course_trainer","duration_of_course","schedule_of_course","course_code","course_syllabus")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("title","description","start_time","end_time")