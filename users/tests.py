from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users import models as u_m


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.create_url = reverse("users:create")
        self.create_data = {
            "email": "user@user.user",
            "password": "1234qweR$",
            "tg_chat_id": "123456789",
        }

        self.get_token_url = reverse("users:get_token")
        self.get_token_data = {"email": "user@user.user", "password": "1234qweR$"}

    def test_create(self):
        response = self.client.post(self.create_url, self.create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(u_m.User.objects.all().exists())

    def test_get_token(self):
        user = u_m.User.objects.create(**self.create_data)
        response = self.client.post(self.get_token_url, self.get_token_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
