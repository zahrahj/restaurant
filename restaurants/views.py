
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm


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


def restaurant_create(request):
	form =RestaurantForm(request.POST or None)
	if form.is_valid():

		form.save()

		return redirect("list")
	context = {

	"form" : form 
	}

	return render(request, "restaurant_create.html", context)



def restaurant_update(request,restaurant_id):

	item = Restaurant.objects.get(id= restaurant_id)
	form = RestaurantForm(instance = item)

	if request.method == "POST":

		form = RestaurantForm(request.POST or None, instance = item)

		
		if form.is_valid():
			form.save()
			return redirect("detail", restaurant_id= restaurant_id)

	context = {

	"form": form,
	"item": item,	

	}

	return render(request, "restaurant_update.html", context)


def restaurant_delete(request,restaurant_id):
	Restaurant.objects.get(id=restaurant_id).delete()

	return redirect("list")
