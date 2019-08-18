from rest_framework.serializers import ModelSerializer, SerializerMethodField
from allies.models import Allies


class AlliesSerializer(ModelSerializer):
    """
    This Serailizer is used to translate django objects to json formats
    Arguments:
        ModelSerializer {[ Serializer ]} -- This helps in translating django objects to json format
    """

    user = SerializerMethodField()

    class Meta:
        model = Allies
        fields = ["user", "user_name", "tracking_id", "total_traffic", "day_expiry"]

    def get_user(self, obj):
        """
        This serializer method is used to return the user that created this object
        Arguments:
            obj {[type]} -- [description]
        Returns:
            str -- 
        """
        return str(obj.user.username) if obj.user else "Anoynmous"
