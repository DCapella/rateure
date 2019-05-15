from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PhotoForm
from .models import Photo

from PIL import Image
import numpy as np
import pickle


class Home(ListView):
    model = Photo
    template_name = 'home.html'

class CreatePhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo.html'
    size = (400, 267)


    try:
        likes = []
        for m in model.objects.all():
            model_id = m.id
            file_name = './media/' + m.photo.name

            img = Image.open(file_name)
            img = img.resize(size)
            test = np.array(img).ravel()
            
            try:
                model_file = './photos/kera_v_0.sav'
                kera = pickle.load(open(model_file, 'rb'))
                likes = int(kera.predict(abs(np.array([test,]))))
                print('='*50)
                print(likes)
                print('='*50)
            except:
                likes = 1

            Photo.objects.filter(id=m.id).update(likes=likes)
    except Exception as e:
        print(e)

    success_url = reverse_lazy('home')