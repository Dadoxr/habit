from typing import Dict, Any
from rest_framework import serializers
from django.conf import settings
from .services import get_object


class MainValidator:
    """
    MainValidator class provides validation rules for habits.
    """

    def make_main_validating(self, serializer, data: Dict[str, Any]) -> None:
        """
        Perform main validation checks on the provided data.

        Args:
            data (Dict[str, Any]): The data to be validated.
        """
        self.validate_rule_1(data)
        self.validate_rule_2(data)
        self.validate_rule_3(data)
        self.validate_rule_4(data)
        self.validate_rule_5(data)

    def validate_rule_1(self, data: Dict[str, Any]) -> None:
        """
        Rule 1: Exclude simultaneous selection of related habit and specifying a reward.

        Args:
            data (Dict[str, Any]): The data to be validated.

        Raises:
            serializers.ValidationError: If the rule is violated.
        """
        related_habit = data.get("related_habit")
        reward = data.get("reward")

        if related_habit and reward:
            raise serializers.ValidationError(
                "Выберите либо связанную привычку, либо укажите вознаграждение, но не оба одновременно."
            )

    def validate_rule_2(self, data: Dict[str, Any]) -> None:
        """
        Rule 2: Time required should not exceed settings.MAX_TIME_REQUIRED seconds.

        Args:
            data (Dict[str, Any]): The data to be validated.

        Raises:
            serializers.ValidationError: If the rule is violated.
        """
        time_required = data.get("time_required")

        if time_required and time_required > settings.MAX_TIME_REQUIRED:
            raise serializers.ValidationError(
                f"Время выполнения должно быть не больше {settings.MAX_TIME_REQUIRED} секунд."
            )

    def validate_rule_3(self, data: Dict[str, Any]) -> None:
        """
        Rule 3: Only habits with the enjoyable attribute can be assigned as related habits.

        Args:
            data (Dict[str, Any]): The data to be validated.

        Raises:
            serializers.ValidationError: If the rule is violated.
        """
        related_habit = data.get("related_habit")

        if related_habit:
            related_habit_pk = related_habit.get("pk")
            related_habit_object = get_object(pk=related_habit_pk)

            if not related_habit_object.enjoyable:
                raise serializers.ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки."
                )

    def validate_rule_4(self, data: Dict[str, Any]) -> None:
        """
        Rule 4: Enjoyable habits cannot have a reward or a related habit.

        Args:
            data (Dict[str, Any]): The data to be validated.

        Raises:
            serializers.ValidationError: If the rule is violated.
        """
        enjoyable = data.get("enjoyable")
        related_habit = data.get("related_habit")
        reward = data.get("reward")
        print(enjoyable, related_habit, reward)

        if enjoyable and (related_habit or reward):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )

    def validate_rule_5(self, data: Dict[str, Any]) -> None:
        """
        Rule 5: Habits cannot be performed less frequently than once every settings.MAX_FREQUENCY days.

        Args:
            data (Dict[str, Any]): The data to be validated.

        Raises:
            serializers.ValidationError: If the rule is violated.
        """
        frequency = data.get("frequency")

        if frequency > settings.MAX_FREQUENCY:
            raise serializers.ValidationError(
                f"Нельзя выполнять привычку реже, чем 1 раз в {settings.MAX_FREQUENCY} дней. "
            )
