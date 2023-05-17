from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
    PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255,)
    is_active = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=False,)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Grid(models.Model):
    """Grid model to store grid points"""
    points = models.TextField(null=False, blank=False,
                              help_text="Semicolon separated values",
                              validators=[
                                RegexValidator(
                                    r"^-?\d+,-?\d+(;-?\d+,-?\d+)*$",
                                    message="Set of points should be "
                                            "semicolon separated"
                                )
                              ])
    closest_points = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def find_closest_points(self):
        point_list = self.points.split(';')

        closest_distance = float('inf')
        closest_points = []

        for i in range(len(point_list)):
            x1, y1 = map(int, point_list[i].split(','))

            for j in range(i+1, len(point_list)):
                x2, y2 = map(int, point_list[j].split(','))

                distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

                if distance < closest_distance:
                    closest_distance = distance
                    closest_points = [point_list[i], point_list[j]]

        return ';'.join(closest_points)

    def save(self, *args, **kwargs):
        self.closest_points = self.find_closest_points()
        return super().save(*args, **kwargs)
