from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    phone = models.CharField(
        verbose_name="Phone",
        help_text="phone number starts from +(your code)xxx-xxx-xx",
        max_length=12,
        unique=True
    )

    gender = models.CharField(
        verbose_name="Gender",
        help_text="Enter your gender",
        max_length=1,
        choices=GENDER_CHOICES
    )


    class Meta:
        ordering = ["-id"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return self.username
