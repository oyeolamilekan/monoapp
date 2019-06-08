from lessons.models import Lesson
from rest_framework.serializers import ModelSerializer


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'category', 'video_url']
