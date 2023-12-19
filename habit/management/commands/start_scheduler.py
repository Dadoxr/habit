import json
from django.utils.timezone import timedelta, now
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def set_schedule(every, period, name, task) -> None:
    """
    Set up a periodic task schedule for Celery.

    Args:
        every: Frequency of the task.
        period: Time period for the task (e.g., IntervalSchedule.MINUTES).
        name: Name for the periodic task.
        task: The task to be scheduled.
    """

    if not (every, period, name, task):
        every = 1
        period = IntervalSchedule.MINUTES
        name = "Send reminder of habit to telegram"
        task = "habit.tasks.check_habit_to_remind"
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=every, period=period
    )
    PeriodicTask.objects.create(
        interval=schedule, name=name, task=task, expires=now() + timedelta(seconds=30)
    )
