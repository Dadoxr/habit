from rest_framework import serializers
from habit import models as h_m, paginators as h_p, validators as h_v


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Habit model.
    """

    class Meta:
        model = h_m.Habit
        fields = (
            "place",
            "time",
            "action",
            "enjoyable",
            "related_habit",
            "frequency",
            "reward",
            "time_required",
            "public",
        )
        pagination_class = h_p.HabitPagination

    def validate(self, data):
        """
        Custom validation method.

        Args:
            data (dict): Dictionary containing the serialized data.

        Returns:
            dict: None.

        Raises:
            serializers.ValidationError: If validation fails.
        """
        validator = h_v.MainValidator()
        validator.make_main_validating(self, data)

        return data
