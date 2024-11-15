# authentication/urls.py
from django.urls import path
from . import views, image_views  # Import the new image_views module
from .start_exam_auth import start_exam_authentication
from .views import get_exam_questions

urlpatterns = [
    path('submit-student-form/', views.submit_student_form, name='submit_student_form'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp_view'),
    path("upload-student-image/", image_views.upload_student_image, name="upload_student_image"),
    path("start-exam/", start_exam_authentication, name='start_exam_authentication'),
    path('get-exam-questions/', get_exam_questions, name='get_exam_questions'),
]





