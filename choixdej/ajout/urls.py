from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ajout, name="ajout"),
    url(r'^accueil.html$', views.accueil, name="accueil"),
	url(r'^confirmation.html$', views.confirmation, name="confirmation"),
    url(r'^deco.html$', views.deconnexion, name="deco")
]
