from django.urls import path

from ..views import feedback

CREATE_FEEDBACK = [
    # Admin routes for the seller.
    path('create_feedback/', feedback.FeedbackCreateAPIView.as_view(), name='create_feedback')
]