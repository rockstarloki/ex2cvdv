from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    clas = models.IntegerField()
    sections = models.CharField(max_length=10)
