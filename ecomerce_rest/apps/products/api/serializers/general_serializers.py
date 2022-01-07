# En aplicaciones grandes este archivo suele ser una carpeta que contiene todos los serializadores
from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('status',)
class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('status',)
class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('status',)