from django.urls import path
from users import apps as u_a, views as u_v
from rest_framework_simplejwt import views

app_name = u_a.UsersConfig.name


urlpatterns = [
    path("create/", u_v.UserCreateAPIView.as_view(), name="create"),
    path("token/", views.TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name="refresh_token"),
]
