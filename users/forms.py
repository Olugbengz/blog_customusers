from typing import Any
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import CustomUser

#  date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'}))  
# SelectDateWidget

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length='100', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length='100', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	date_of_birth = forms.DateField(label="", required=False, widget=forms.NumberInput(attrs={'type': 'date', 'class':'form-control', 'placeholder':'yyyy-mm-dd (DOB)'}))
	password1 = forms.CharField(label='Password', min_length=8, max_length=50, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', min_length=8, max_length=50, widget=forms.PasswordInput)
	
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2']

	
	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-white small"> <li>Your password can\'t be too similar to your personal information</li> <li>Your password must be at leaset eight digit long.</li></ul>' 

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<ul class="form-text text-white small"> <li>Your password must match!</li></ul>'  

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if (password1 and password2) and password1 != password2:
			raise ValidationError("Passwords don't match, retype the passwords.")
		return password2

	def save(self, commit=True):

		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class CustomUserChangeForm(UserChangeForm):

	password = ReadOnlyPasswordHashField()

	class Meta:
		model = CustomUser
		fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'is_admin']






