from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def creat_user(self,)


class User(AbstractBaseUser):
    pass
