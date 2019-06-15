from rest_framework.serializers import ModelSerializer

from findit.models import Products
from tags.models import Catergories



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'image', 'source_url',
                  'genre', 'shop_rel', 'price', 'description')


# Catergory serializer


class CatergoriesSerializer(ModelSerializer):
    class Meta:
        model = Catergories
        fields = ('id', 'title', 'tags')
