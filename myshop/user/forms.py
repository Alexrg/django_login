from django import forms

class UserLogin(forms.Form):
	"""
	Creates a form of two input fields so the user can enter a coordinate.
	"""
	user = forms.CharField(label='user')
	password = forms.CharField(label='password', widget=forms.PasswordInput)