from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(max_length=10)
    roll_number=models.CharField(max_length=10)
    student_email=models.EmailField(max_length=25)
    nationality_choices=(
    ("Kenyan","Kenyan"),
    ("Ugandan","Ugandan"),
    ("Rwandeese","Rwandees"),
    ("South Sudaneese","South Sudaneese"))
    nationality=models.CharField(max_length=15,choices=nationality_choices)
    student_id=models.CharField(max_length=18)
    id_number=models.CharField(max_length=18)
    gender_choices=(
        ("Female","Female"),
        ("Male","Male")
    )
    gender=models.CharField(max_length=6,choices=gender_choices)
    phone_number=models.CharField(max_length=16)
    county=models.CharField(max_length=12)
    profile=models.ImageField(upload_to="media")
    medical_report=models.FileField(upload_to="media")
    date_of_enrollment=models.DateField(max_length=8)
    # course_name=models.CharField(max_length=10)
    language_choices=(
        ("English","English"),
        ("Kiswahili","Kiswahili")
    )
    language=models.CharField(max_length=10,choices=language_choices)

    # serial_number=models.CharField(max_length=10, blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
