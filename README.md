# custom-user-model-Django

1. Create `CustomUser` model by extending from `AbstractBaseUser`.
2. Create `CustomeUserManager` by extending from `BaseUserManager`.
3. Add to `setings` as `AUTH_USER_MODEL = app.user`.
4. Make changes in *admin.py*, i.e. creating creations and change form for the user in the admin panel.
