from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    # measure_unit = serializers.StringRelatedField() #Model.__str()
    # category_product = serializers.StringRelatedField() #Model.__str()

    class Meta:
        model = Product
        exclude = ('status','created_date','modificated_date','deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,
        }