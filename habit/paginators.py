from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """
    Custom pagination settings for the Habit model.
    """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 25
