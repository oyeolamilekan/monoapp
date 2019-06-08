from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'created')

    def get_user(self, obj):
        return str(obj.user.username) if obj.user else 'Anoynmous'


# Catergory serializer
