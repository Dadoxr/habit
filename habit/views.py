from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit import services as h_sv, serializers as h_sl, permissions as h_p


class HabitPublicListAPIView(generics.ListAPIView):
    """
    API view for listing public habits.

    This view provides a list of habits that are marked as public.

    Attributes:
        serializer_class: The serializer class for serializing habit objects.
        permission_classes: The permission classes required to access this view.
        queryset: The queryset representing habits marked as public.

    """

    serializer_class = h_sl.HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = h_sv.get_objects().filter(public=True)


class HabitUserListAPIView(generics.ListAPIView):
    """
    API view for listing user-specific habits.

    This view provides a list of habits associated with the authenticated user.

    Attributes:
        serializer_class: The serializer class for serializing habit objects.
        permission_classes: The permission classes required to access this view.
        queryset: The initial queryset representing all habits.

    Methods:
        get_queryset: Returns the queryset filtered by the authenticated user.

    """

    serializer_class = h_sl.HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = h_sv.get_objects()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class HabitCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a new habit.

    This view allows users to create a new habit, and additional actions
    are performed after the object is successfully created.

    Attributes:
        serializer_class: The serializer class for validating and creating habit objects.
        permission_classes: The permission classes required to access this view.

    Methods:
        perform_create: Performs additional actions after object creation.

    """

    serializer_class = h_sl.HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save the object and set the user
        habit_instance = serializer.save(user=self.request.user)

        # Additional actions after object creation
        text = f"Задача делать {habit_instance} создана"
        h_sv.send_message(self.request.user.tg_chat_id, text)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating an existing habit.

    This view allows users to update an existing habit, and additional actions
    are performed after the object is successfully updated.

    Attributes:
        serializer_class: The serializer class for validating and updating habit objects.
        queryset: The initial queryset representing all habits.
        permission_classes: The permission classes required to access this view.

    Methods:
        put: Handles PUT requests for updating the habit.
        patch: Handles PATCH requests for partially updating the habit.

    """

    serializer_class = h_sl.HabitSerializer
    queryset = h_sv.get_objects()
    permission_classes = [h_p.IsOwnerOrStaff, IsAuthenticated]

    def put(self, request, *args, **kwargs):
        self.object = super().get_queryset()
        response = self.update(request, *args, **kwargs)

        text = f'Задача "{self.object}" изменена'
        h_sv.send_message(self.request.user.tg_chat_id, text)

        return response

    def patch(self, request, *args, **kwargs):
        self.object = super().get_queryset()
        response = self.partial_update(request, *args, **kwargs)

        text = f'Задача "{self.object}" изменена'
        h_sv.send_message(self.request.user.tg_chat_id, text)

        return response


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    API view for deleting an existing habit.

    This view allows users to delete an existing habit, and additional actions
    are performed after the object is successfully deleted.

    Attributes:
        queryset: The initial queryset representing all habits.
        permission_classes: The permission classes required to access this view.

    Methods:
        delete: Handles DELETE requests for deleting the habit.

    """

    queryset = h_sv.get_objects()
    permission_classes = [h_p.IsOwnerOrStaff, IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        self.object = super().get_queryset()

        text = f"Задача делать {self.object} удалена"
        h_sv.send_message(self.request.user.tg_chat_id, text)

        return self.destroy(request, *args, **kwargs)
