from django.shortcuts import render, redirect, get_object_or_404
from app1.models import schl_students, schl_teachers
from app1.forms import StudentForm, TeacherForm


def home(request):
    return render(request, 'frontend/home.html', {
        'page': 'home'
    })


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


def delete_entry(request, type, id):
    if type == "student":
        get_object_or_404(schl_students, id=id).delete()
    elif type == "teacher":
        get_object_or_404(schl_teachers, id=id).delete()
    return redirect('total')
