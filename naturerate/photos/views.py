from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .forms import PhotoForm
from .models import Photo

from PIL import Image
import numpy as np
import pickle


def Home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})

def CreatePhotoView(request):
    if request.method == 'POST':
        size = (400, 267)
        form = PhotoForm(request.POST, request.FILES)
        # title = form.get('title')
        # photo = form.get('photo')
        title = request.POST['title']
        photo = request.FILES['photo']

        img = Image.open(photo)
        img = img.resize(size)
        test = np.array(img).ravel()
        version = 1
        model_file = f'./AI/kera_v_{version}.sav'
        kera = pickle.load(open(model_file, 'rb'))
        pred = kera.predict(abs(np.array([test,])))
        likes = int(abs(pred/74.1319))

        new_photo = Photo.objects.create(
            title=title,
            photo=photo,
            likes=likes
        )

        return redirect('home')
    else:
        form = PhotoForm()

    return render(request, 'photo.html', {'form': form})