from django.urls import path
from django.conf.urls import url

from .views import Home, CreatePhotoView

urlpatterns = [
    path('', Home, name='home'),
    path('photo/', CreatePhotoView, name='add_photo'),
]