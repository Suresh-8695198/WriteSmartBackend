# authentication/urls.py
from django.urls import path
from . import views
from . import views, image_views  

urlpatterns = [
    
    path('submit-student-form/', views.submit_student_form, name='submit_student_form'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp_view'),
    path("upload-student-image/", image_views.upload_student_image, name="upload_student_image"),  # New endpoint for image upload
]
