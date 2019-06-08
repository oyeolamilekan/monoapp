from rest_framework.serializers import ModelSerializer

from findit.models import Products
from tags.models import Catergories



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'image', 'source_url',
                  'genre', 'shop', 'price', 'slug', 'description')


# Catergory serializer


class CatergoriesSerializer(ModelSerializer):
    class Meta:
        model = Catergories
        fields = ('id', 'title', 'tags')
