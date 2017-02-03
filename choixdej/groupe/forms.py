from django import forms

class CreerGroupeForm(forms.Form):
	nomgroupe = forms.CharField(label="Nom groupe", max_length=50)
