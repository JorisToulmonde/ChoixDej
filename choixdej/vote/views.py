from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def vote(request):
    return render(request, 'vote/vote.html')

def deconnexion(request):
	logout(request)
	return redirect('../index')

def accueil(request):
	return redirect('../home')
