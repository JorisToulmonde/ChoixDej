from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def ajout(request):
    return render(request, 'ajout/ajout.html')

def accueil(request):
    return redirect('../home')

def deconnexion(request):
	logout(request)
	return redirect('../index')
