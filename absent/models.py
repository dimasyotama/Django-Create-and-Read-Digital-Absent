from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class Student(models.Model):
    gender_choices = (
        ('Male','Male'),
        ('Female', 'Female'),
    )
    course_choices = (
        ('Ipa','Ipa'),
        ('Ips','Ips'),
        ('Bahasa','Bahasa'),
    )
    hexw = models.CharField(max_length=22)
    name = models.CharField(max_length=120)
    kelas = models.CharField(max_length=90)
    gender = models.CharField(max_length=20,choices=gender_choices,default='Male')
    course = models.CharField(max_length=20,choices=course_choices,default='Ipa')
    def __unicode__(self):
        return self.name

