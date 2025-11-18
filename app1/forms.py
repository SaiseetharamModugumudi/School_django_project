from django import forms

from app1.models import schl_students, schl_teachers
class StudentForm(forms.ModelForm):
    class Meta:
        model = schl_students
        fields = '__all__'

        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = schl_teachers
        fields = '__all__'
    