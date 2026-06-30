from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from students.models import Student
from teachers.models import Teacher

# Create your views here.
def home(request):
    return render(request, "home.html")

def login_page(request):
    
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            return redirect("student_dashboard")

        else:
            return render(request, "login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")

def admin_dashboard(request):

    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()

    context = {
        "total_students": total_students,
        "total_teachers": total_teachers,
    }

    return render(request, "admin/dashboard.html", context)

def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html")

def student_dashboard(request):
    return render(request, "student/dashboard.html")

def logout_page(request):
    logout(request)
    return redirect("home")