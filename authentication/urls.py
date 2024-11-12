from django.urls import path
from . import views

urlpatterns = [
    path('test-firebase/', views.test_firebase_connection, name='test_firebase_connection'),
]
