from django.shortcuts import render
from .models import *
from .backend import *

# Create your views here.
def index(request):
    if request.method=="GET":
        videos=Video.objects.all()
        print(videos)


        return render(request,"index.html",{"videos":videos})

def upload(request):
    if request.method=="POST":
        print(request.POST)
        print("hello world")
        print(request.FILES)
        print("checking \n")
        print(request.FILES['video'])
        print(request.FILES['thumbnail'])
        x=Video.objects.create(video1thumbnail=request.FILES['thumbnail'],video_title=request.POST['videoTitle'],video_desc=request.POST['description'],video=request.FILES['video'])

        return render(request,"videoupload.html")
    else:
        return render(request,"videoupload.html")




def video(request,id):
    video=Video.objects.get(id=id)
    print(video)
    print(video.video.url)
    print(video.video1thumbnail)
    print(video.video_title)
    return render(request,"video.html",{"video":video})

