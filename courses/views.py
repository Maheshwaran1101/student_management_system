from django.shortcuts import render, redirect
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def add_course(request):

    if request.method == "POST":

        Course.objects.create(
            course_name=request.POST["course_name"],
            course_code=request.POST["course_code"],
            duration=request.POST["duration"],
        )

        return redirect("course_list")

    return render(request, "courses/add_course.html")


def edit_course(request, id):

    course = Course.objects.get(id=id)

    if request.method == "POST":

        course.course_name = request.POST["course_name"]
        course.course_code = request.POST["course_code"]
        course.duration = request.POST["duration"]

        course.save()

        return redirect("course_list")

    return render(request, "courses/edit_course.html", {"course": course})


def delete_course(request, id):

    course = Course.objects.get(id=id)

    course.delete()

    return redirect("course_list")