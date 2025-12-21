from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),
    path('student/', views.student_view, name='student'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('total/', views.total_data, name='total'),

    path('update/<str:type>/<int:id>/', views.update_entry, name='update_entry'),
    path('delete/<str:type>/<int:id>/', views.delete_entry, name='delete_entry'),
]
