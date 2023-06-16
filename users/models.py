# Django
from django.contrib.auth.models import (
    UserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
from django.core.validators import(
    RegexValidator,
)
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, name, surname, email, phone_number, password, **extra_fields):
        """
        Create and save a user in the database with user information (name, surname, email, phone number and password).
        
        Returns:
            user: Instance of the user model.
        """
        
        fields = {'name':name, 'surname':surname, 'email':email, 'phone number':phone_number}
        for key, value in fields.items():
            if not value:
                raise ValueError(f"The given {key} must be set")
        user = self.model(
            name=name,
            surname=surname,
            email=self.normalize_email(email),
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, name=None, surname=None, email=None, phone_number=None,  password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, surname, email, phone_number, password, **extra_fields)
    
    def create_superuser(self, name=None, surname=None, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(name, surname, email, phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class that implements a user model with all roles with permissions supported by the administrator.
    """
    
    name = models.CharField(
        _("name"),
        null=False,
        blank=False,
        max_length=90,
    )
    surname = models.CharField(
        _("surname"),
        null=False,
        blank=False,
        max_length=90,
    )
    email = models.EmailField(
        _('email'),
        null=False,
        blank=False,
        unique=True,
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,4}){1,2}$",
                message=_('Invalid email.'),
            )
        ]
    )
    phone_number = models.CharField(
        _('phone number'),
        null=False,
        blank=False,
        unique=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\(\+\d{1,3}\)\s?\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}$',
                message=_('Invalid phone number.')
            )
        ]
    )
    password = models.CharField(
        _("password"), 
        max_length=128,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    is_active = models.BooleanField(
        _("is active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone_number']
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def get_full_name(self) -> str:
        """
        Return the first and last name, with a space in between.
        """
    
        return f'{self.name.capitalize()} {self.surname.capitalize()}'

