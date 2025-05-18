from django.urls import path
from .import views

urlpatterns = [path('newsself',views.newsself,name='newsself'),
               path('add/',views.addphoto,name='addphoto'),]