from rest_framework import serializers
from users import models as u_m


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        model = u_m.User
        fields = ("email", "password", "tg_chat_id")
