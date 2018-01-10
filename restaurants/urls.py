from django.contrib import admin
from django.urls import path

from restaurants import views
# this is a urls page

urlpatterns = [
    
    path('detail/<int:restaurant_id>/', views.restaurant_detail, name= "detail"),
    path('list/', views.restaurant_list, name= "list"),

]