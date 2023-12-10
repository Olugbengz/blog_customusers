from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
	# email = forms.EmailField(label='Email')
	# first_name = forms.CharField(label='First Name', max_length=120)
	# last_name = forms.CharField(label='Last Name', max_length=120)
	# date_of_birth = forms.DateField(required=False)
	password1 = forms.CharField(label='Password', min_length=8, max_length=50, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', min_length=8, max_length=50, widget=forms.PasswordInput)
	
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'email', 'date_of_birth']

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






