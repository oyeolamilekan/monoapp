"""
    This serializer handles the serialization of the store object
"""
from rest_framework.serializers import ModelSerializer

from shop.models import Shop


class ShopSerializer(ModelSerializer):
    """[the shop info]

    Arguments:
        {[ inherits from serializer class rest framework]} -- [description]
    """

    class Meta:
        model = Shop
        fields = (
            "id",
            "user",
            "slug",
            "title",
            "categories",
            "phone_number",
            "address",
            "description",
            "logo",
        )
