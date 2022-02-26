from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from rest_framework.response import Response

from apps.products.models import MeasureUnit


class MeasureUnitViewSet(viewsets.GenericViewSet):
    '''
    Unidad de medida
    '''
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status = True)

    def list(self, request):
        '''
        Método para listar (comentario externo)


        (comentario interno)
        :param request:
        name --> El nombre de la unidad de medida
        :return:
        '''
        data = self.get_queryset()
        data = self.get_serializser(data, many=True)
        return Response(data.data)

class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status = True)

    def list(self, request):
        '''
        Método para listar indicadores


        (comentario interno)
        :param request:
        name --> El nombre del indicador
        :return:
        '''
        data = self.get_queryset()
        data = self.get_serializser(data, many=True)
        return Response(data.data)

class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer