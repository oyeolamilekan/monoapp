from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.serializers.feedback import FeedbackSerializer
from feedbacks.models import FeedBacks


class FeedbackCreateAPIView(CreateAPIView):
    """[Create the feedback object]

    Arguments:
        CreateAPIView {[ Class ]} -- [ inherits from DRF class ]
    """
    queryset = FeedBacks.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
