from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseUserManager(models.Manager):
    @classmethod
    def normalize_username(cls, phone_number):
        """
        Normalize the username by lowercasing it.
        """
        phone_number = phone_number or ""
        if len(phone_number) < 4:
            raise ValueError(_('username must have at least 4 characters'))
        return phone_number.lower()

    def get_by_natural_key(self, phone_number):
        return self.get(**{self.model.USERNAME_FIELD: phone_number})


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not phone_number:
            raise ValueError(_('Users must have a phone_number'))

        user = self.model(
            phone_number=self.normalize_username(phone_number)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user