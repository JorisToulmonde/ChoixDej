from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.rejoindre, name="rejoindre"),
    url(r'^creer.html$', views.creer, name="creer"),
	url(r'^confirmation.html$', views.confirmation, name="confirmation"),
	url(r'^confirmationrej.html$', views.confirmationrej, name="confirmationrej"),
	url(r'^existepas.html$', views.existepas, name="existepas"),
	url(r'^existe.html$', views.existe, name="existe"),
	url(r'^fav.html$',views.fav,name='fav'),
]
