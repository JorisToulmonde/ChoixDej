from django.shortcuts import render
from django.http import HttpResponse
from index.forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Create your views here.

def index(request):

    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('../home')
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'index/index.html', {'form':form})
