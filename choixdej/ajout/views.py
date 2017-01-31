from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from ajout.forms import AjoutForm
from ajout.models import Restaurant
from django.http import HttpResponseRedirect
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = AjoutForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = Restaurant()
            restaurant.titre = form.cleaned_data["titre"]
            restaurant.adresse = form.cleaned_data["adresse"]
            restaurant.image = form.cleaned_data["image"]
            restaurant.save()
            return HttpResponseRedirect('confirmation.html')
    else:
        form = AjoutForm()

    return render(request, 'ajout/ajout.html', {'form': form})

def accueil(request):
    return redirect('../home')

def confirmation(request):
    return render(request, 'ajout/confirmation.html')

def deconnexion(request):
	logout(request)
	return redirect('../index')
