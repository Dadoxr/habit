from django.urls import path
from habit import apps, views

app_name = apps.HabitConfig.name

urlpatterns = [
    path("", views.HabitPublicListAPIView.as_view(), name="list"),
    path("my/", views.HabitUserListAPIView.as_view(), name="my_list"),
    path("create/", views.HabitCreateAPIView.as_view(), name="create"),
    path("update/<int:pk>", views.HabitUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>", views.HabitDestroyAPIView.as_view(), name="delete"),
]
