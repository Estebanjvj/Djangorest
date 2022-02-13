from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def delete(self, request, pk=None):
        # soft delete al reescribir esto
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.status = False
            product.save()
            return Response({'msg':'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)