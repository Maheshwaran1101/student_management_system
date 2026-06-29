from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
    return render(render, "admin/dashboard.html")

def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html")

def student_dashboard(request):
    return render(request, "student/dashboard.html")

def logout_page(request):
    logout(request)
    return redirect("home")