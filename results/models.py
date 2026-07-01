from django.db import models
from students.models import Student
from courses.models import Course


class Result(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    subject = models.CharField(max_length=100)

    marks = models.IntegerField()

    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.subject}"
