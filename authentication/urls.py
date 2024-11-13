# authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('submit-student-form/', views.submit_student_form, name='submit_student_form'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp_view'),

]
