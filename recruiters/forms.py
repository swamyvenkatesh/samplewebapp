from django import forms

class Searchform(forms.Form):
	search = forms.CharField(max_length=100,min_length=20)