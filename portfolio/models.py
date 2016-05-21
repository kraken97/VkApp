from django.contrib.admin import ModelAdmin
from django.db import models


# Create your models here.
from django.forms import widgets

dir="static/images"
class Images(models.Model):
    name = models.CharField(max_length=500)
    img_src = models.ImageField(default="-" ,upload_to=dir)
    img_link = models.CharField(max_length=400, default="-")
    img_description = models.CharField(max_length=500)
    
    list_display = ['image_scr']


    def  img(self):
        return u'<img src="/%s" style="max-width:200px;max-height:200px"/>' % (self.img_src.name)
    img.short_description = 'Image'
    img.allow_tags = True
    def __str__(self):
        return self.name


class Albums(models.Model):
    name = models.CharField(max_length=500)
    image = models.ManyToManyField(Images)
    album_description = models.CharField(max_length=500)
    date = models.DateField(auto_created=True)
    def __str__(self):
        return self.name
