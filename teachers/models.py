from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"