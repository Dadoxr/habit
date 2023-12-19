from rest_framework import generics
from habit import models as h_m
from telegram import services as t_s


def get_object(pk: int):
    """
    Get a single habit object by its primary key.

    Args:
        pk: Primary key of the habit object.

    Returns:
        Habit: The habit object.

    Raises:
        Http404: If the object with the given primary key does not exist.
    """
    return generics.get_object_or_404(h_m.Habit, pk=pk)


def get_objects():
    """
    Get all habit objects.

    Returns:
        QuerySet: A queryset containing all habit objects.
    """
    return h_m.Habit.objects.all()


def create_object(data: dict):
    return h_m.Habit.objects.create(**data)


def send_message(chat_id: int, text: str):
    """
    Send a message to Telegram.

    Args:
        chat_id: Telegram chat ID.
        text: The text of the message.
    """
    t_s.send_message_to_telegram(chat_id, text)
