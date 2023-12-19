from celery import shared_task
from django.utils.timezone import now
from telegram import services as t_s
from habit import services as h_sv


@shared_task
def check_habit_to_remind():
    """
    Celery task to check habits and send reminders.

    Returns:
        str: A message indicating the completion of the task.
    """

    habits_to_send = h_sv.get_objects().filter(time=now().time())
    for habit in habits_to_send:
        chat_id = habit.user.tg_chat_id
        text = f"Я буду {habit}"
        t_s.send_message_to_telegram(chat_id, text)

    return "Рассылка завершена"
