
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def restaurant_list (resquest):
	objects = Restaurant.objects.all()

	context = {
	"objects" : objects
	}

	return render (resquest, 'restaurant_list.html', context)



def restaurant_detail (resquest, restaurant_id):

	detail = Restaurant.objects.get(id = restaurant_id)

	context = {
	"restaurant": detail
	}

	return render (resquest, 'restaurant_details.html', context)
