from django.contrib import admin
from django.urls import path
from .views import TestCreateView,MedicalTestDetailView
app_name="diagonsis"

urlpatterns = [
    path('',TestCreateView.as_view(),name='upload_test' ),
    path('test-result/<int:pk>/', MedicalTestDetailView.as_view(), name='test_detail'),

]