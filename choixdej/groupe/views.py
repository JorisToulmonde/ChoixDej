from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from index.models import Groupes, Restaurant
from groupe.forms import CreerGroupeForm
# Create your views here.

def rejoindre(request):
    allgroupes = Groupes.objects.filter(nom_utilisateur_id=request.user.id)
    if request.method == 'POST':
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

    return render(request, 'groupe/rejoindre.html', {'allgroupes':allgroupes})

def creer(request):
    if request.method == 'POST':
        form = CreerGroupeForm(request.POST, request.FILES)
        if form.is_valid():
            gr = Groupes()
            ng = form.cleaned_data["nomgroupe"]
            requete = Groupes.objects.filter(nom_groupes=ng)
            if not requete:
                print("coucou1")
                gr.nom_groupes = ng
                gr.nom_utilisateur_id = request.user.id
                gr.save()
                return HttpResponseRedirect('confirmation.html')
            else:
                print("coucou2")
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

def existedeja(request):
    return render(request, 'groupe/existedeja.html')

def confirmationrej(request):
    return render(request, 'groupe/confirmationrej.html')
