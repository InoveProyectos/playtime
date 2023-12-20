from django.contrib import admin
from stock.models import Articulo, Categoria, Deposito, Stock


# Registro de los modelos en el admin

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):

    fieldsets = (
       (None, {
           'fields': ('nombre', 'codigo', 'categoria', 'precio_unitario')
       }),
       ('Advanced options', {
           'classes': ('collapse',),
           'fields': ('lote', 'vto', 'punto_de_reorden')
       })
    )
    list_display = ('nombre', 'codigo', 'categoria', 'precio_unitario', 'punto_de_reorden')
    search_fields = ['nombre']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    fields = ('nombre',)


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    fields = ('nombre',)


@admin.register(Stock)
class DepositoAdmin(admin.ModelAdmin):
    fields = ('articulo', 'deposito', 'cantidad')
    list_display = ('articulo', 'deposito', 'cantidad')
    list_filter = ('deposito',)
    search_fields = ['articulo']


# Modificación en título de panel de administración
admin.site.site_header = 'PlayTime - Sitio de Administración -'

# Modificación en leyenda de la pestaña de la hoja
admin.site.site_title = 'Playtime'
admin.site.index_title = 'Control de stock'
