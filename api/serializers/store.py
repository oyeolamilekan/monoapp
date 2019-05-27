from rest_framework import serializers
from shop.models import Shop


class ShopCreateSerializer(serializers.Serializer):
    shop = serializers.CharField()

    def validate_shop(self, data):
        return True

class ShopSerializer(serializers.ModelSerializer):
    """[Serializers the shop info]

    Arguments:
        serializers {[ inherits from serializer class rest framework]} -- [description]
    """
    class Meta:
        model = Shop
        fields = ('id', 'user', 'slug', 'title', 'categories','phone_number',
                  'address', 'description', 'logo')
