from django.forms import ModelForm
from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['name','kelas','gender','course']