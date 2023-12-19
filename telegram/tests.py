from django.conf import settings
from rest_framework.test import APITestCase
from unittest.mock import patch
import requests
from telegram import services as t_s 

class TelegramUtilsTest(APITestCase):
    @patch('telegram.services.requests.post')
    def test_send_message_to_telegram_success(self, mock_post):
        mock_post.return_value.json.return_value = {"ok": True}

        chat_id = settings.ADMIN_TELEGRAM_CHAT_ID
        text = "Test message"
        result = t_s.send_message_to_telegram(chat_id, text)

        mock_post.assert_called_with(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

        self.assertEqual(result, {"ok": True})

    @patch('telegram.services.requests.post')
    def test_send_message_to_telegram_failure(self, mock_post):
        mock_post.return_value.json.return_value = {"ok": False, "description": "Test error"}

        chat_id = settings.ADMIN_TELEGRAM_CHAT_ID
        text = "Test message"
        result = t_s.send_message_to_telegram(chat_id, text)

        mock_post.assert_called_with(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

        self.assertIsNone(result)

    @patch('telegram.services.requests.post', side_effect=requests.RequestException)
    def test_send_message_to_telegram_exception(self, mock_post):
        chat_id = settings.ADMIN_TELEGRAM_CHAT_ID
        text = "Test message"
        result = t_s.send_message_to_telegram(chat_id, text)

        mock_post.assert_called_with(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

        self.assertIsNone(result)
