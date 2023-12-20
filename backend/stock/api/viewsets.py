from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import (ArticuloSerializer, CategoriaSerializer, DepositoSerializer, StockSerializer,
                           FormulaSerializer)


# Se elije trabajar con viewsets debido a que estas clases seguramente necesitarán crear, modificar y
# eliminar instancias, por lo que ahorramos mucho codigo en lugar de hacer una apiView para cada una de 
# las funciones.
class ArticuloViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticuloSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self, request):
        articulos = self.get_serializer(self.get_queryset(), many=True)
        return Response(articulos.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Artículo creado correctamente'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        articulo = self.get_queryset().filter(id=pk).first()
        if articulo:
            articulo.delete()
            return Response({'message': 'El artículo fue eliminado con éxito'}, status= status.HTTP_200_OK)
        return Response({'message': 'No existe ese artículo para ser eliminado'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            articulo = self.serializer_class(self.get_queryset(pk), data=request.data)
            if articulo.is_valid():
                articulo.save()
                return Response(articulo.data, status=status.HTTP_200_OK)
            return Response(articulo.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class DepositoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DepositoSerializer
    queryset = serializer_class.Meta.model.objects.all()


class StockViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StockSerializer
    queryset = serializer_class.Meta.model.objects.all()


class FormulaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FormulaSerializer
    queryset = serializer_class.Meta.model.objects.all()