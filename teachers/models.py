from django.db import models

from courses.models import Course

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
 
    course = models.ForeignKey(
    Course,
    on_delete=models.CASCADE
 )
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"