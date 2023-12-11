from django.db import models

# Create your models here.

class Categoria(models.Model):
    '''
    Esta clase hereda de django models.Model, y crea una tabla llamada categorias,
    para almacenar las distintas categorias asignada a cada uno de los articulos.
    '''
    nombre = models.CharField(max_length=60, unique=True, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombre
    

class Articulo(models.Model):
    '''
    Genera una tabla que almacena articulos, y cada columna recibe el nombre de cada atributo
    '''
    nombre = models.CharField(max_length=60, verbose_name='Nombre articulo')
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=60)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    punto_de_reorden = models.PositiveIntegerField(default=0) 
    # El punto de reorden es la cantidad minima de un artículo, a partir de la cual se debe
    # hacer una solicitud de reposicion.
    #  
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
        ordering = ['nombre']

    def __str__(self):
        '''
        La función str representa lo que retorna cuando llamamos al objeto
        '''
        return self.nombre
