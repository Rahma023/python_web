from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Events


class School_Events_Form(forms.ModelForm):
    class Meta:
        model=Events
        fields="__all__"
        # widgets={
        #     "first_name":forms.TextInput(attrs={"class":"form-control"}),
        #     "last_name":forms.TextInput(attrs={"class":"form-control"}),
        #     "age":forms.NumberInput(attrs={"class":"form-control"}),
        #     "date_of_birth":forms.DateInput(attrs={"class":"form-control"}),
        #     "roll_number":forms.NumberInput(attrs={"class":"form-control"}),
        #     "student_email":forms.TextInput(attrs={"class":"form-control"}),
        #     "nationality":forms.Select(attrs={"class":"form-control"}),
        #     "student_id":forms.NumberInput(attrs={"class":"forms-control"}),
        #     "id_number":forms.NumberInput(attrs={"class":"form-control"}),
        #     "gender":forms.Select(attrs={"class":"form-control"}),
        #     "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
        #     "county":forms.TextInput(attrs={"class":"form-control"}),
        #     "medical_report":forms.FileInput(attrs={"class":"form-control"}),
        #     "date_of_enrollment":forms.DateInput(attrs={"class":"form-control"}),
        #     "course_name":forms.TextInput(attrs={"class":"form-control"}),
        #     "language":forms.Select(attrs={"class":"form-control"}),
        #     "serial_number":forms.NumberInput(attrs={"class":"form-control"}),

        # }
