from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.roll_number} - {self.first_name} {self.last_name}"
