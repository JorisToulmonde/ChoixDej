from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from index.models import Restaurant, Groupes
from django.db.models import Max
from django.db import connection
from collections import namedtuple
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def namedtuplefetchall(cursor):
	desc = cursor.description
	nt_result = namedtuple('Result',[col[0] for col in desc], rename=True)
	return [nt_result(*row) for row in cursor.fetchall()]

@csrf_protect
def home(request):
	#id de l'utilisateur connecte
    idg = request.user.id
    image = Restaurant.objects.raw('SELECT * from index_restaurant join index_groupes using(nom_groupes) where score = (SELECT max(score) FROM index_restaurant join index_groupes using(nom_groupes) where nom_utilisateur_id=%s ) and nom_utilisateur_id=%s LIMIT 1',([idg],[idg]))
    jyvais = Groupes.objects.raw('SELECT * FROM index_groupes JOIN auth_user ON index_groupes.nom_utilisateur_id=auth_user.id WHERE favori=1 AND nom_groupes = ANY(SELECT nom_groupes FROM index_groupes WHERE nom_utilisateur_id=%s)',[idg])
    if request.method=="POST":
        if 'jyvais' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE index_groupes SET favori = 1 WHERE nom_utilisateur_id = %s",[idg])
                return HttpResponseRedirect('../home')
        elif 'jyvaispas' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE index_groupes SET favori = 0 WHERE nom_utilisateur_id = %s",[idg])
                return HttpResponseRedirect('../home')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * from index_restaurant join index_groupes using(nom_groupes) where score = (SELECT max(score) FROM index_restaurant join index_groupes using(nom_groupes) where nom_utilisateur_id=%s ) and nom_utilisateur_id=%s LIMIT 1',([idg],[idg]))
        result = namedtuplefetchall(cursor)

        if result[0].anciennete != 0:
    	    cursor.execute("UPDATE index_restaurant SET anciennete = 0 , frequence = frequence+1 where id = %s",[result[0].id])

    #Renvoie le restaurant choisi a afficher sur la page home.html
    return render_to_response('home/home.html', {'image':image, 'jyvais':jyvais}, context_instance=RequestContext(request))

def deconnexion(request):
	logout(request)
	return redirect('../index')

def groupe(request):
    return redirect('../groupe')

def vote(request):
    return redirect('../vote')

def ajoutrestaurant(request):
    return redirect('../ajout')
