from django.db import models

# Create your models here.
class ListaPares(models.Model):
    TALLAS = [(str(i), str(i)) for i in range(34, 42)]
    orden_pedido = models.ForeignKey('OrdenPedido', related_name='lista_pares', on_delete=models.CASCADE)
    talla = models.CharField(max_length=2, choices=TALLAS)
    pares = models.IntegerField(default=0)

class OrdenPedido(models.Model):
    orden_pedido = models.CharField(max_length=10, unique=True)
    bloque = models.CharField(max_length=6)
    fecha_orden = models.DateField()
    fecha_entrega = models.DateField(blank=True)
    cliente = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    total_pares = models.IntegerField(editable=False)
    foto_orden = models.ImageField(upload_to='ordenes/', blank=True)

    def save(self, *args, **kwargs):
        self.total_pares = self.lista_pares.all().aggregate(models.Sum('pares'))['pares__sum'] or 0
        super().save(*args, **kwargs)
    