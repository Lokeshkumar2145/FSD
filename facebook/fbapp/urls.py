from django.urls import path,include
from .views import *


urlpatterns = [

    path("",dashboard,name='dashboard'),
    path("home/",home,name='home'),
    path("logout/",handle_logout,name='logout'),
    path("signup/",signup,name="signup"),
    path("login/",signin,name="signin"),
    path("like/<uid>/",liked,name='like'),
    path("cmt/<id>/",comments,name='comments'),
    path("delete-comment/<id>/",delete_commennt,name='delete_cmt'),
    path("all-feed/",all_feed,name='all_feed'),

   
]

