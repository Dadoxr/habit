from django.conf import settings
import requests


def send_message_to_telegram(chat_id, text):
    """
    Function to send a message to a Telegram chat using the Telegram Bot API.

    Args:
        chat_id: The identifier of the chat to which the message should be sent.
        text: The text of the message.

    Returns:
        dict: The JSON response from the Telegram API.

    Note:
        If an error occurs during the process, the function prints an error message
        and returns None.
    """

    params = {"chat_id": chat_id, "text": text}
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        result = response.json()

        if not result["ok"]:
            raise Exception(
                f"Ошибка при отправке сообщения в Telegram: {result.get('description')}"
            )

        return result
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения в Telegram: {e}")
        return None
