from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from habit import services as h_sv


class TestHabit:
    def __init__(self, user, enjoyable, related_habit=None) -> None:
        self.user = user
        self.place = "testplace"
        self.time = now().time()
        self.action = "testaction"
        self.enjoyable = enjoyable
        self.related_habit = related_habit
        self.frequency = 1
        self.reward = "testreward"
        self.time_required = 120
        self.public = False

    def get_habit_data(self):
        self.habit_data = {
            "user": self.user,
            "place": self.place,
            "time": self.time,
            "action": self.action,
            "enjoyable": self.enjoyable,
            "frequency": self.frequency,
            "reward": self.reward,
            "time_required": self.time_required,
            "public": self.public,
        }
        if self.related_habit:
            self.habit_data.update({"related_habit": self.related_habit})
        return self.habit_data


class HabitAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email="testuser", password="testpass"
        )
        self.client.force_authenticate(user=self.user)

    def test_public_habits_list(self):
        url = reverse("habit:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_habits_list(self):
        url = reverse("habit:my_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        url = reverse("habit:create")
        data = TestHabit(user=self.user, enjoyable=False).get_habit_data()
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_habit(self):
        data = TestHabit(user=self.user, enjoyable=False).get_habit_data()
        habit = h_sv.create_object(data)
        url = reverse("habit:update", kwargs={"pk": habit.pk})
        data.update({"name": "Updated Habit", "public": False})
        response = self.client.put(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_habit(self):
        data = TestHabit(user=self.user, enjoyable=False).get_habit_data()
        habit = h_sv.create_object(data)
        url = reverse("habit:update", kwargs={"pk": habit.pk})
        data.update({"name": "Updated Habit"})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        data = TestHabit(user=self.user, enjoyable=False).get_habit_data()
        habit = h_sv.create_object(data)
        url = reverse("habit:delete", kwargs={"pk": habit.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
