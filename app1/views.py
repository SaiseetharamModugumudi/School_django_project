from django.shortcuts import render, redirect, get_object_or_404
from app1.models import schl_students, schl_teachers
from app1.forms import StudentForm, TeacherForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'frontend/home.html', {'page': 'home'})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm_password']

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'auth/register.html')



def student_view(request):
    form = StudentForm(request.POST or None)
    students = schl_students.objects.all()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student')

    return render(request, 'frontend/home.html', {
        'page': 'student',
        'students': students,
        'student_form': form
    })


def teacher_view(request):
    form = TeacherForm(request.POST or None)
    teachers = schl_teachers.objects.all()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('teacher')

    return render(request, 'frontend/home.html', {
        'page': 'teacher',
        'teachers': teachers,
        'teacher_form': form
    })


def total_data(request):
    students = schl_students.objects.all()
    teachers = schl_teachers.objects.all()
    return render(request, 'frontend/home.html', {
        'page': 'total',
        'students': students,
        'teachers': teachers
    })


def update_entry(request, type, id):
    if type == "student":
        entry = get_object_or_404(schl_students, id=id)
        form = StudentForm(request.POST or None, instance=entry)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('total')
        return render(request, 'frontend/update.html', {'form': form, 'type': 'student'})

    elif type == "teacher":
        entry = get_object_or_404(schl_teachers, id=id)
        form = TeacherForm(request.POST or None, instance=entry)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('total')
        return render(request, 'frontend/update.html', {'form': form, 'type': 'teacher'})


@login_required(login_url='login')
def delete_entry(request, type, id):
    if request.method == "POST":
        password = request.POST.get('password')
        user = authenticate(
            username=request.user.username,
            password=password
        )

        if user is None:
            return render(request, 'frontend/confirm_delete.html', {
                'error': 'Incorrect password'
            })

        # Password correct → delete record
        if type == "student":
            get_object_or_404(schl_students, id=id).delete()
        elif type == "teacher":
            get_object_or_404(schl_teachers, id=id).delete()

        return redirect('total')

    return render(request, 'frontend/confirm_delete.html')
