from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('homesatu/get/<int:homesatu_id>/', views.homesatu,name='homesatu'),
    path('category/',views.category,name='category'),
    path('category/get/<int:category_id>/', views.cat,name='cat'),
]

