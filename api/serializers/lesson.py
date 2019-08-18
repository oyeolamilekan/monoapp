"""
    This serializer handles the serialization of the lessons object
"""
from rest_framework.serializers import ModelSerializer

from lessons.models import Lesson


class LessonSerializer(ModelSerializer):
    """
    This Serailizer is used to translate django objects to json formats
    Arguments:
        ModelSerializer {[ Serializer ]} -- This helps in translating django objects to json format
    """

    class Meta:
        model = Lesson
        fields = ["id", "title", "category", "video_url"]
