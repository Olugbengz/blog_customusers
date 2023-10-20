from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser

	list_display = ["email", "first_name", "last_name", "date_of_birth", "is_staff", "is_active", "is_admin"]
	list_filter = ["is_admin"]
	fieldsets = [
		(None, {
			"fields": ["email", "password"]}),
		("Personal info", {"fields": ["first_name", "last_name", "date_of_birth"]}),
		("Permissions", {"fields": ["is_staff", "is_active", "is_admin"]}),
		]
	add_fieldsets = [
		(None, {
			"classes": ["wide"],
			"fields":
				["email", "first_name", "last_name", "date_of_birth", "password1", "password2"],},), ]

	ordering = ["email"]
	search_fields = ["email"]
	filter_horizontal = []


admin.site.register(CustomUser, CustomUserAdmin)