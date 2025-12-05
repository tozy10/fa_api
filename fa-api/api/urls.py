from django.urls import path
from .views import imageUploadView
from django.conf.urls.static import static

urlpatterns = [
    
    path("upload/", imageUploadView),
]