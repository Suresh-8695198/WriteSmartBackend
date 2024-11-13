# authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('submit-student-form/', views.submit_student_form, name='submit_student_form'),
]
