from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name="homepage"),
    url(r'^deco.html$', views.deconnexion, name="deco"),
    url(r'^groupe.html$', views.groupe, name="groupe"),
    url(r'^ajout.html$', views.ajoutrestaurant, name="ajoutrestaurant"),
    url(r'^vote.html$', views.vote, name="vote")
]
