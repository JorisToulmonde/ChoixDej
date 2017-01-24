from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from inscription.forms import ConnexionForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse

# Create your views here.

def connexion(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password1 = form.cleaned_data["password1"]
			password2 = form.cleaned_data["password2"]
			email = form.cleaned_data["email"]

			user = User.objects.create_user(username, email, password1)
			user.save()
			return redirect('../index')

	else:
		form = ConnexionForm()
	return render(request,'inscription/inscription.html', {'form':form})
