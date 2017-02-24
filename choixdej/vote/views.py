from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from index.models import Groupes, Restaurant
# Create your views here.
def vote(request):
    idg = request.user.id
    allresto = Restaurant.objects.raw('SELECT * FROM index_restaurant JOIN index_groupes USING(nom_groupes) WHERE favori = 1 AND nom_utilisateur_id=%s',[idg])
    return render(request, 'vote/vote.html', {'allresto': allresto})

def deconnexion(request):
	logout(request)
	return redirect('../index')
