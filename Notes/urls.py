from django.contrib import admin
from django.urls import path, include, re_path
from . import views



urlpatterns = [path('', views.home, name='home'),
 path('delete/<str:id>', views.delete, name='delete'),
               path('update/<str:id>', views.update, name='update'),

]