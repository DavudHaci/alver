from django.contrib import admin
from django.urls import path

from . import views

app_name="user"
                        #MENBE
urlpatterns = [       #Funkisya Adi Backend 
                        #  |
                      #    ^
    path('register/', views.register,name="register"),
    path('login/', views.LoginUser,name="login"),
    path('logout/', views.UserLogout,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('sticker/', views.sticker,name="sticker"),
]
