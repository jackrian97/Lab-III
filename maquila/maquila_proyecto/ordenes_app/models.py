from django.db import models

from django.db import models

# Modelo para almacenar las tallas y el número de pares para cada talla en una orden de pedido
class ListaPares(models.Model):
    # Lista de tallas predefinidas
    TALLAS = [(str(i), str(i)) for i in range(34, 42)]

    # Clave externa que establece la relación con la orden de pedido
    orden_pedido = models.ForeignKey('OrdenPedido', related_name='lista_pares', on_delete=models.CASCADE)
    
    # Campo de selección para la talla
    talla = models.CharField(max_length=2, choices=TALLAS)
    
    # Número de pares para la talla especificada
    pares = models.IntegerField(default=0)

    class Meta:
        db_table = 'lista_pares'  # Nombre de la tabla en la base de datos


# Modelo para almacenar la información de una orden de pedido
class OrdenPedido(models.Model):
    # Número único de la orden de pedido
    orden_pedido = models.CharField(max_length=10, unique=True)
    
    # Bloque de números de ordenes de pedidos que salen por día
    bloque = models.CharField(max_length=6)
    
    # Fecha en que se emitió la orden de pedido
    fecha_orden = models.DateField()
    
    # Fecha de entrega de la orden de pedido (opcional)
    fecha_entrega = models.DateField(blank=True)
    
    # Cliente que realiza la orden de pedido
    cliente = models.CharField(max_length=50)
    
    # Referencia del producto para la orden de pedido
    referencia = models.CharField(max_length=50)
    
    # Total de pares en la orden de pedido (se calculará automáticamente)
    total_pares = models.IntegerField(editable=False)
    
    # Imagen de la orden de pedido (opcional)
    foto_orden = models.ImageField(upload_to='ordenes/', blank=True)

    # Método para calcular el total de pares en la orden de pedido
    def save(self, *args, **kwargs):
        self.total_pares = self.lista_pares.all().aggregate(models.Sum('pares'))['pares__sum'] or 0
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'orden_pedido'
    