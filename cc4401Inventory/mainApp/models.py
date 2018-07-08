from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Correo Electronico'), unique=True)
    first_name = models.CharField(_('Nombre'), max_length=30, blank=True)
    last_name = models.CharField(_('Apellido'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Fecha de Registro'), auto_now_add=True)
    is_active = models.BooleanField(_('Activo'), default=True)
    avatar = models.ImageField(upload_to='static/img/avatars/', null=True, blank=True)
    enabled = models.BooleanField('Habilitado', default=True)
    rut = models.CharField('RUT', max_length=12, unique=True, null=True)
    role = models.IntegerField('Tipo', default=0)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Item(models.Model):
    name = models.CharField('Nombre', max_length=40)
    description = models.TextField('Descripción', blank=True)
    image = models.ImageField('Imagen del articulo', upload_to='static/img/items', blank=True)

    class Meta:
        abstract = True


class Action(models.Model):
    STATES = (
        ('A', 'Aceptado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente')
    )
    starting_date_time = models.DateTimeField()
    ending_date_time = models.DateTimeField()
    state = models.CharField('Estado', choices=STATES, max_length=1, default='P')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
