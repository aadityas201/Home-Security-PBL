from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models


class UserManager(BaseUserManager):
    #extending the BaseUserManager class
    def create_user(self, email, password=None, name=None, mobile_no=None):
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(
            email), mobile_no=mobile_no, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, name=None, mobile_no=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password, name, mobile_no)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
#                   'twitter': 'twitter', 'email': 'email'}


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email_address',
                              max_length=255, unique=True, db_index=True)
    mobile_no = models.CharField(
        max_length=12, unique=True, verbose_name='mobile_no')
    name = models.CharField(max_length=100, verbose_name='Name')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auth_provider = models.CharField(
    #     max_length=255, blank=False,
    #     null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile_no', 'name']

    objects = UserManager()

    def __str__(self):
        return self.email
