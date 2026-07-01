from django import forms
from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:

        model = Result

        fields = "__all__"

        widgets = {

            "student": forms.Select(attrs={"class":"form-control"}),

            "course": forms.Select(attrs={"class":"form-control"}),

            "subject": forms.TextInput(attrs={"class":"form-control"}),

            "marks": forms.NumberInput(attrs={"class":"form-control"}),

            "grade": forms.TextInput(attrs={"class":"form-control"}),

        }