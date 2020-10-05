from django.contrib import admin
from django.urls import path

from . import views

app_name="post"

urlpatterns = [
    path('create/', views.create,name="create"),
    path('delete/<int:id>', views.deleteArticle,name="delete"),
   # path('update/<int:id>', views.updateArticle,name="update"),

]
