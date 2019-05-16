from django.db import models


class Photo(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='images/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title