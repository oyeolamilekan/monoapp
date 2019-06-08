from django.urls import path

from ..views import lesson

LESSON_URL = [
    # Tutorial routes for the merchants.
    path('lesson/<slug:slug>/', lesson.LessonListAPI.as_view(), name='lesson')
]
