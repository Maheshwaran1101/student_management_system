from django.shortcuts import render, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()

    return render(request, "students/student_list.html", {
        "students": students
    })


def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            roll_number=request.POST["roll_number"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            department=request.POST["department"],
            year=request.POST["year"],
            address=request.POST["address"],
        )

        return redirect("student_list")

    return render(request, "students/add_student.html")


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.first_name = request.POST["first_name"]
        student.last_name = request.POST["last_name"]
        student.roll_number = request.POST["roll_number"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.department = request.POST["department"]
        student.year = request.POST["year"]
        student.address = request.POST["address"]

        student.save()

        return redirect("student_list")

    return render(request, "students/edit_student.html", {
        "student": student
    })


def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect("student_list")