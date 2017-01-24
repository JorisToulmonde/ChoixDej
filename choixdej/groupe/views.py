from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def rejoindre(request):
    return render(request, 'groupe/rejoindre.html')

def creer(request):
	return render(request, 'groupe/creer.html')

def deconnexion(request):
	logout(request)
	return redirect('../index')

def accueil(request):
	return redirect('../home')
