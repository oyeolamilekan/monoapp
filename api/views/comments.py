from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from comment.models import Comment
from api.serializers.comments import CommentSerializer
from lessons.models import Lesson


@api_view(["POST"])
def create_comment(request, slug, content_type):
    """
    [This view creates the comments by geting the content type that needs to be created under]
    
    Arguments:
        request {[ request objects ]} -- [The request sent from the client]
        slug {[ string ]} -- [Used to filter the model objects comments would relate to]
        content_type {[ string ]} -- [Checks the kind of model that would be related to the comment object]
    
    Returns:
        [Json] -- [It returns a json response]
    """
    lesson = Lesson.objects.get(id=slug)
    comment = Comment(
        content_object=lesson, text=request.data["textbox_value"], user=request.user
    )
    comment.save()
    comment_serialized = CommentSerializer(comment)
    return Response(status=status.HTTP_200_OK, data=comment_serialized.data)


@api_view(["GET"])
def get_comments(request, slug, content_type):
    """
    [Get the comments related to the model called]

    Arguments:
        request {[ request objects ]} -- [ The request response from python]
        slug {[ string ]} -- [Used to filter the models where the comments would relate to]
        content_type {[ string ]} -- [Checks the kind of model that needs to written underneath]
    
    Returns:
        [Json] -- [It returns a json response]
    """
    lesson = Lesson.objects.get(id=slug)
    comments = lesson.comments.all()
    comment_list = CommentSerializer(comments, many=True)
    return Response(status=status.HTTP_200_OK, data=comment_list.data)
