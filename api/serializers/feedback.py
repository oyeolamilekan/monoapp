from feedbacks.models import FeedBacks
from rest_framework.serializers import ModelSerializer


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedBacks
        fields = ['score', 'title', 'body']
