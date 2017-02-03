from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from index.models import Restaurant
from django.db.models import Max
# Create your views here.

def home(request):
    idg = request.user.id
    image = Restaurant.objects.raw('SELECT * from index_restaurant join index_groupes using(nom_groupes) where score = (SELECT max(score) FROM index_restaurant join index_groupes using(nom_groupes) where nom_utilisateur_id=%s ) and nom_utilisateur_id=%s LIMIT 1',([idg],[idg]))
    return render(request, 'home/home.html', {'image':image})

def deconnexion(request):
	logout(request)
	return redirect('../index')

def groupe(request):
    return redirect('../groupe')

def vote(request):
    return redirect('../vote')

def ajoutrestaurant(request):
    return redirect('../ajout')
