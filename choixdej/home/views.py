from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from ajout.models import Restaurant
from django.db.models import Max
# Create your views here.

def home(request):
    image = Restaurant.objects.raw('SELECT * FROM ajout_restaurant WHERE score = (SELECT max(score) FROM ajout_restaurant) LIMIT 1')
    return render(request, 'home/home.html', {'image':image})

def deconnexion(request):
	logout(request)
	return redirect('../index')

def groupe(request):
    return render(request, 'groupe/rejoindre.html')

def vote(request):
    return redirect('../vote')

def ajoutrestaurant(request):
    return redirect('../ajout')
