from django.db import models

# Create your models here.

class Student(models.Model):
    university_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    std_id = models.IntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    