from django.db.models import Q
from rest_framework.generics import ListAPIView

from api.pagination.lesson import LessonPageNumberPagination
from api.serializers.lesson import LessonSerializer
from lessons.models import Lesson


class LessonListAPI(ListAPIView):
    serializer_class = LessonSerializer
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = LessonPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Lesson.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
