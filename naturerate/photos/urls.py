from django.urls import path

from .views import Home, CreatePhotoView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('photo/', CreatePhotoView.as_view(), name='add_photo'),
]