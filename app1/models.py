from django.db import models

# Create your models here.
class schl_students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)


class schl_teachers(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    experience_years = models.IntegerField()
    gender = models.CharField(max_length=10)

