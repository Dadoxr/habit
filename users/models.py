from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Main User model for the application.

    Attributes:
        email (EmailField): The email address of the user (unique).
        tg_chat_id (PositiveBigIntegerField): Telegram Chat ID of the user.
    """

    username = None
    email = models.EmailField(verbose_name="email", unique=True)
    tg_chat_id = models.PositiveBigIntegerField(
        verbose_name="Telegram Чат ID", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return a string representation of the user."""
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        verbose_name = "юзер"
        verbose_name_plural = "юзеры"
