from django.shortcuts import render, redirect
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()

    return render(request, "teachers/teacher_list.html", {
        "teachers": teachers
    })


def add_teacher(request):

    if request.method == "POST":

        Teacher.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            employee_id=request.POST["employee_id"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            subject=request.POST["subject"],
            qualification=request.POST["qualification"],
        )

        return redirect("teacher_list")

    return render(request, "teachers/add_teacher.html")


def edit_teacher(request, id):

    teacher = Teacher.objects.get(id=id)

    if request.method == "POST":

        teacher.first_name = request.POST["first_name"]
        teacher.last_name = request.POST["last_name"]
        teacher.employee_id = request.POST["employee_id"]
        teacher.email = request.POST["email"]
        teacher.phone = request.POST["phone"]
        teacher.subject = request.POST["subject"]
        teacher.qualification = request.POST["qualification"]

        teacher.save()

        return redirect("teacher_list")

    return render(request, "teachers/edit_teacher.html", {
        "teacher": teacher
    })


def delete_teacher(request, id):

    teacher = Teacher.objects.get(id=id)

    teacher.delete()

    return redirect("teacher_list")