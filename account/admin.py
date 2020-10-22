from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django import forms

from account.models import User

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError('Password not match')
		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ['email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff']

	def clean_password(self):
		return self.initial['password']


class UserAdmin(BaseUserAdmin):
	# form to add and change user in Admin
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ['email', 'first_name', 'last_name', 'is_staff']
	list_filter = ['is_staff']
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_active', 'is_staff')}),
	)

	add_fieldsets  = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)