from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from comment.models import Comment
from api.serializers.comments import CommentSerializer
from lessons.models import Lesson


@api_view(['POST'])
def create_comment(request, slug, content_type):
    lesson = Lesson.objects.get(id=slug)
    comment = Comment(content_object=lesson,
                      text=request.data['textbox_value'], user=request.user)
    comment.save()
    comment_serialized = CommentSerializer(comment)
    return Response(status=status.HTTP_200_OK, data=comment_serialized.data)


@api_view(['GET'])
def get_comments(request, slug, content_type):
    lesson = Lesson.objects.get(id=slug)
    comments = lesson.comments.all()
    comment_list = CommentSerializer(comments, many=True)
    return Response(status=status.HTTP_200_OK, data=comment_list.data)
