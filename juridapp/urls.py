from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_student, name='create_student'),
    path('detail/<int:id>/', views.student_detail, name='student_detail'),
]
