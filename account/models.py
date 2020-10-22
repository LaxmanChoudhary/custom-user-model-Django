# for model fields
from django.db import models

# to override Base User model,
# WARNING! to be done at very start of the project
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# custom manager created for the user
from account.manager import UserManager

# check below for necessary methods to define
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#specifying-a-custom-user-model
class User(AbstractBaseUser, PermissionsMixin):
	email= models.EmailField(verbose_name='email address', unique=True)
	first_name = models.CharField(verbose_name='first name', max_length=126)
	last_name = models.CharField(verbose_name='last name', max_length=126, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name='user'
		verbose_name_plural = 'users'

	def get_full_name(self):
		full_name = '{} {}'.format(self.first_name, self.last_name)
		return self.full_name

	def get_short_name(self):
		return self.first_name