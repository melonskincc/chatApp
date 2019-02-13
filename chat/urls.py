from django.urls import path, re_path
from chat import views

urlpatterns = [
    path('index/', views.index, name='首页'),
    re_path(r'^(?P<roomName>[^/]+)/$', views.room, name='房间'),
]
