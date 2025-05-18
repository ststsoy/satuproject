from django.urls import path
from .import views

urlpatterns = [
    path('insvid/', views.home,name='home'),
]
