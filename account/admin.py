# register the new user model, to make it editable from the admin panel
from django.contrib import admin
from django.contrib.auth.models import Group

# djangos default admin permissions and methods here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# to make fields available when adding new user
from django import forms

# import new User model
from account.models import User

# additional classes
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#a-full-example
# just like form !!!!!
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
		# process through the super class, but don't save as commit is False,
		user = super().save(commit=False)


		user.set_password(self.cleaned_data['password1'])

		# if commit is True, save the data to database
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

# unregister group, if not needed
admin.site.unregister(Group)