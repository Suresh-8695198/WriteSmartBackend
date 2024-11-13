# authentication/urls.py
from django.urls import path
from . import views, image_views  # Import the new image_views module

urlpatterns = [
    path("submit-student-form/", views.submit_student_form, name="submit_student_form"),
    path("upload-student-image/", image_views.upload_student_image, name="upload_student_image"),  # New endpoint for image upload
]
