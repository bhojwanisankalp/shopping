from django import forms
from .models import Product, Guest


class ProductForm(forms.ModelForm):
	""" Django form to create Products """
	class Meta:
		model = Product
		exclude = ['created_at', 'updated_at']


class GuestForm(forms.ModelForm):
	""" Django form to create Guest Records """
	class Meta:
		model = Guest
		exclude = ['created_at', 'updated_at']
    		