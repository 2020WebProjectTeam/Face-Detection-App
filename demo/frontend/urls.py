from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/image/', views.picupload),
    path('camera/', views.camera),
    path('test/', views.camera),
    path('upload/', views.upload),
]