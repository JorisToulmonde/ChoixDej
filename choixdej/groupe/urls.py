from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.rejoindre, name="rejoindre"),
    url(r'^creer.html$', views.creer, name="creer"),
    url(r'^accueil.html$', views.accueil, name="accueil"),
    url(r'^deco.html$', views.deconnexion, name="deco")
]
