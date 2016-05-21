from django.shortcuts import render

# Create your views here.
from portfolio.models import Albums, Images


def index(req):

    albums=[]

    for album in Albums.objects.all().values():
        print(album['id'])
        data={'data':Images.objects.filter(albums=album['id']) ,'album': album }
        albums.append(data)

    print(albums)
    return  render(req, 'portfolio/index.html',{'albums':albums})
