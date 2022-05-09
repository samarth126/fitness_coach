from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),

    path('cool/',views.cool, name="cool"),
    path('cam_but/',views.cam_but, name="cam_but"),

    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('login/', views.loginr, name='loginr'),
    
    path('profile/', views.profilee, name='profile'),

    path('health/', views.health, name='health'),
    path('noti/', views.noti, name='noti'),
    path('contact/', views.contactt, name='contactt'),

    path('food/', views.food1, name='food'),

    path('result/', views.result, name='result'),
    path('web/', views.web, name='web'),

]