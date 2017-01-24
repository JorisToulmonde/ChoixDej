from django import forms

class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	email = forms.EmailField(label="Votre adresse mail")
	password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Validation mot de passe", widget=forms.PasswordInput)

	def clean(self):
		 cleaned_data = super(ConnexionForm, self).clean()
		 password1 = cleaned_data.get("password1")
		 password2 = cleaned_data.get("password2")
		 if not (password1 == password2):
			 raise forms.ValidationError("Les mots de passe ne sont pas identiques.")
