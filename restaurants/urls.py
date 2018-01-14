from django.contrib import admin
from django.urls import path

from restaurants import views
# this is a urls page

urlpatterns = [
    
    path('detail/<int:restaurant_id>/', views.restaurant_detail, name= "detail"),
    path('list/', views.restaurant_list, name= "list"),
    path('update/<int:restaurant_id>/', views.restaurant_update, name= "restaurant_update"),
    path('delete/<int:restaurant_id>/', views.restaurant_delete, name= "restaurant_delete"),
    path('create/', views.restaurant_create, name= "restaurant_create"),




]