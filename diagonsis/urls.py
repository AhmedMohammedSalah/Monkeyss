from django.contrib import admin
from django.urls import path
from .views import TestCreateView
app_name="diagonsis"

urlpatterns = [
    path('',TestCreateView.as_view(),name='upload_test' ),
]