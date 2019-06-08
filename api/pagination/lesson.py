from rest_framework.pagination import PageNumberPagination


class LessonPageNumberPagination(PageNumberPagination):
    page_size = 10
