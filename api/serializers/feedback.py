from feedback.models import Feedback
from rest_framework.serializers import ModelSerializer


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['score', 'title', 'body']
