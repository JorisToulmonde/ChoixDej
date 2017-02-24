from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from ajout.forms import AjoutForm
from index.models import Restaurant, Groupes
from django.http import HttpResponseRedirect
from django.db import connection
from collections import namedtuple
# Create your views here.

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result',[col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def ajout(request):
    if request.method == 'POST':
        form = AjoutForm(request.POST, request.FILES)
        if form.is_valid():
            idg = request.user.id
            restaurant = Restaurant()
            restaurant.nom_restaurant = form.cleaned_data["titre"]
            restaurant.adresse_restaurant = form.cleaned_data["adresse"]
            restaurant.image = form.cleaned_data["image"]
            restaurant.frequence = 0
            restaurant.anciennete = 10
            with connection.cursor() as cursor:
            #cursor = connections['choixdejj'].cursor()
                cursor.execute('SELECT nom_groupes FROM index_groupes where favori = 1 AND  nom_utilisateur_id = %s', [idg])
                result = namedtuplefetchall(cursor)
                restaurant.nom_groupes = result[0].nom_groupes
            restaurant.save()
            return HttpResponseRedirect('confirmation.html')
    else:
        form = AjoutForm()

    return render(request, 'ajout/ajout.html', {'form': form})

def accueil(request):
    return redirect('../home')

def confirmation(request):
    return render(request, 'ajout/confirmation.html')
