
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('upload/',views.upload,name='upload'),
    path("video/<int:id>/", views.video, name="video"),
]