from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

        widgets = {
            "course_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "course_code": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "duration": forms.TextInput(
                attrs={"class": "form-control"}
            ),
        }