from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True

	# helper functions for common actions in create_user and create_superuser
	# **extra_fields contain the rest of the args
	def _create_user(self, email, password, is_staff, **extra_fields):
		if not email:
			raise ValueError('Email must be set!')
		email = self.normalize_email(email)
		user = self.model(email=email, is_staff=is_staff, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	# required
	def create_user(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, False, **extra_fields)

	# required
	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must be set True')
		return self._create_user(email, password, True, **extra_fields)