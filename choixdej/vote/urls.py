from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.vote, name="vote"),
    url(r'^deco.html$', views.deconnexion, name="deco")
]
