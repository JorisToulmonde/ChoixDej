from django import forms

class AjoutForm(forms.Form):
	titre = forms.CharField(label="titre", max_length=100)
	adresse = forms.CharField(label="adresse", max_length=100)
	image = forms.ImageField()
