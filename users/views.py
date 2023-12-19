from rest_framework import generics
from users import serializers as u_sl


class UserCreateAPIView(generics.CreateAPIView):
    """
    API view for creating new users.
    """

    serializer_class = u_sl.UserSerializer
