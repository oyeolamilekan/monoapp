from rest_framework.serializers import ModelSerializer, Serializer, CharField

from shop.models import Shop


class ShopCreateSerializer(Serializer):
    shop = CharField()

    def validate_shop(self, data):
        return True

class ShopSerializer(ModelSerializer):
    """[the shop info]

    Arguments:
        {[ inherits from serializer class rest framework]} -- [description]
    """
    class Meta:
        model = Shop
        fields = ('id', 'user', 'slug', 'title', 'categories','phone_number',
                  'address', 'description', 'logo')
