from django.urls import path
from .views import imageUploadview

urlpatterns = [
    
    path("upload/", imageUploadview.as_view()),
]
