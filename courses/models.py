from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    duration = models.CharField(max_length=30)

    def __str__(self):
        return self.course_name