from django.db import models
from users import models as u_m


class Habit(models.Model):
    """
    Model representing a habit.
    """

    user = models.ForeignKey(
        u_m.User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="habits",
        verbose_name="Пользователь",
    )
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.TextField(verbose_name="Действие")
    enjoyable = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    frequency = models.PositiveIntegerField(
        default=1, verbose_name="Периодичность (в днях)"
    )
    reward = models.CharField(max_length=255, verbose_name="Вознаграждение")
    time_required = models.PositiveBigIntegerField(
        verbose_name="Время на выполнение (в секундах)"
    )
    public = models.BooleanField(default=False, verbose_name="Признак публичности")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_habits",
        verbose_name="Связанная привычка",
    )

    def __str__(self):
        """Return a string representation of the habit."""
        return f"{self.action} в {self.time} в {self.place}"

    class Meta:
        """Metadata for the Habit model."""

        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
