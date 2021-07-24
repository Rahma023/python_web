from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(max_length=10)
    roll_number=models.CharField(max_length=10)
    student_email=models.EmailField(max_length=25)
    nationality=models.CharField(max_length=15)
    student_id=models.CharField(max_length=18)
    id_number=models.CharField(max_length=18)
    gender=models.CharField(max_length=6)
    phone_number=models.CharField(max_length=16)
    county=models.CharField(max_length=12)
    profile=models.ImageField()
    medical_report=models.FileField()
    date_of_enrollment=models.DateField(max_length=8)
    course_name=models.CharField(max_length=10)
    language=models.CharField(max_length=10)
    serial_number=models.CharField(max_length=10)
