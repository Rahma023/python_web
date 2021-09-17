from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=12,null=True)
    course_trainer=models.CharField(max_length=12,null=True)
    duration_of_course=models.CharField(max_length=12,null=True)
    schedule_of_course=models.FileField(null=True)
    course_code=models.CharField(max_length=12)
    course_syllabus=models.TextField(null=True)
    # course_desription=models.TextField(null=True)
