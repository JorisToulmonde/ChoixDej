from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def deconnexion(request):
	logout(request)
	return redirect('../index')

def groupe(request):
    return render(request, 'groupe/rejoindre.html')

def vote(request):
    return redirect('../vote')

def ajoutrestaurant(request):
    return redirect('../ajout')
