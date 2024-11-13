# authentication/urls.py
from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    
    path('submit-student-form/', views.submit_student_form, name='submit_student_form'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp_view'),

=======
from . import views, image_views  # Import the new image_views module

urlpatterns = [
    path("submit-student-form/", views.submit_student_form, name="submit_student_form"),
    path("upload-student-image/", image_views.upload_student_image, name="upload_student_image"),  # New endpoint for image upload
>>>>>>> de2f632cfe500c70e678ba15635cf77120f31139
]
