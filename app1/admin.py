from django.contrib import admin
from app1.models import schl_students, schl_teachers
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'section', 'gender')   
    search_fields = ('name', 'grade', 'section')
    list_filter = ('grade', 'section', 'gender')
    
admin.site.register(schl_students, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'experience_years', 'gender')   
    search_fields = ('name', 'subject')             
    list_filter = ('subject', 'gender')
    ordering = ('experience_years',)

admin.site.register(schl_teachers, TeacherAdmin)    
        