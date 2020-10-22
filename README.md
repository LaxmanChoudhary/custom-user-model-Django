# custom-user-model-Django

1. Create `CustomUser` model by extending from `AbstractBaseUser`.
2. Create `CustomeUserManager` by extending from `BaseUserManager`.
3. Add to `setings` as `AUTH_USER_MODEL = app.user`.
4. Make changes in *admin.py*, i.e. creating creations and change form for the user in the admin panel.

## How to check the model
- **Primitive way**<br>
*by using shell*

- **Django way**<br>
We can use admin panel which comes preloaded with every django project.<br>
1. Create admin/superuser by running `python manage.py createsuperuser`

2. Log in to admin-panel @`http://127.0.0.1:8000/admin`(on your localhost) using superuser credentials.

---
Enjoy !
