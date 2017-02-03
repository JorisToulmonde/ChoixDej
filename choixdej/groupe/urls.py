from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.rejoindre, name="rejoindre"),
    url(r'^creer.html$', views.creer, name="creer"),
	url(r'^confirmation.html$', views.confirmation, name="confirmation"),
	url(r'^confirmationrej.html$', views.confirmationrej, name="confirmationrej"),
	url(r'^existedeja.html$', views.existedeja, name="existedeja"),
	url(r'^existe.html$', views.existe, name="existe"),
]
