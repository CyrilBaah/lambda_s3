from django.urls import path
from .views import FileUploadAPIView

urlpatterns = [
    path('', FileUploadAPIView.as_view(), name="fileupload")
]
