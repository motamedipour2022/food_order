from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def creat_user(self, first_name, last_name, username, email, password=None):
        


class User(AbstractBaseUser):
    pass
