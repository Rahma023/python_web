from django.db import models

# Create your models here.

class Trainers(models.Model):
    first_name=models.CharField(max_length=12, null=True , blank=True)
    last_name=models.CharField(max_length=12, null=True , blank=True)
    age=models.PositiveSmallIntegerField( null=True , blank=True)
    date_hired=models.DateField(max_length=10,null=True, blank=True)
    email_address=models.EmailField(max_length=25, null=True , blank=True)
    nationality_choices=(
    ("Kenyan","Kenyan"),
    ("Ugandan","Ugandan"),
    ("Rwandeese","Rwandees"),
    ("South Sudaneese","South Sudaneese"))
    nationality=models.CharField(max_length=15,choices=nationality_choices, null=True , blank=True)
    national_id=models.CharField(max_length=18, null=True , blank=True)
    gender_choices=(
        ("Female","Female"),
        ("Male","Male")
    )
    gender=models.CharField(max_length=6,choices=gender_choices, null=True , blank=True)
    phone_number=models.CharField(max_length=16, null=True , blank=True)
    county=models.CharField(max_length=12, null=True , blank=True)
    profile=models.ImageField(upload_to="media" ,null=True, blank=True)
    qualification=models.CharField(max_length=200, null=True, blank=True)
    occupation=models.CharField(max_length=30, null=True , blank=True)
    date_hired=models.DateField(max_length=8, null=True , blank=True)
    contract=models.FileField(null=True, blank=True)
    language_choices=(
        ("English","English"),
        ("Kiswahili","Kiswahili")
    )
    language=models.CharField(max_length=10,choices=language_choices, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    