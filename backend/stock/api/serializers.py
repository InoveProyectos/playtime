from rest_framework import serializers
from stock.models import Articulo, Categoria, Deposito, Stock, Formula



class ArticuloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Articulo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'categoria': instance.categoria.nombre,
            'codigo': instance.codigo,
            'precio_unitario': instance.precio_unitario,
            'punto_de_reorden': instance.punto_de_reorden,
            'vto': instance.vto,
            'lote': instance.lote
        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('__all__')


class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = ('articulo', 'deposito', 'cantidad')


class FormulaSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer
    
    class Meta:
        model = Formula
        fields = ('__all__')