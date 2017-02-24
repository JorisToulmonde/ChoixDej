from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from index.models import Groupes, Restaurant
from groupe.forms import CreerGroupeForm
from django.db import connection
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_protect
# Create your views here.


@csrf_protect
def rejoindre(request):
    allgroupes = Groupes.objects.filter(nom_utilisateur_id=request.user.id)
    idg = request.user.id
    if request.method == 'POST':
        if 'quitter' in request.POST:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM index_groupes WHERE nom_utilisateur_id = %s",[idg])
                return HttpResponseRedirect('../groupe')
        else:
            print(request.POST.dict())
            form = CreerGroupeForm(request.POST, request.FILES)
            if form.is_valid():
                gr = Groupes()
                ng = form.cleaned_data["nomgroupe"]
                requete = Groupes.objects.filter(nom_groupes=ng)
                if not requete:
                    return HttpResponseRedirect('existepas.html')
                else:
                    gr.nom_groupes = ng
                    gr.nom_utilisateur_id = request.user.id
                    gr.save()
                    return HttpResponseRedirect('confirmationrej.html')
    else:
        form =CreerGroupeForm()
    return render_to_response('groupe/rejoindre.html', {'allgroupes':allgroupes}, context_instance=RequestContext(request))


def creer(request):
    if request.method == 'POST':
        form = CreerGroupeForm(request.POST, request.FILES)
        if form.is_valid():
            gr = Groupes()
            ng = form.cleaned_data["nomgroupe"]
            requete = Groupes.objects.filter(nom_groupes=ng)
            if not requete:
                gr.nom_groupes = ng
                gr.nom_utilisateur_id = request.user.id
                gr.save()
                return HttpResponseRedirect('confirmation.html')
            else:
                return HttpResponseRedirect('existe.html')
    else:
        form =CreerGroupeForm()

    return render(request, 'groupe/creer.html')

def ajoutrestaurant(request):
    return redirect('../ajout')

def confirmation(request):
    return render(request, 'groupe/confirmation.html')

def existe(request):
    return render(request, 'groupe/existe.html')

def existepas(request):
    return render(request, 'groupe/existepas.html')

def confirmationrej(request):
    return render(request, 'groupe/confirmationrej.html')
