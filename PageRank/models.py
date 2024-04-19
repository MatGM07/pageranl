from django.db import models
from django.contrib.auth.models import User
from CarritoApp.models import Producto  # Importa el modelo de Producto desde tu aplicación

class Transition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='link_transitions')
    source_product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='source_transitions')
    destination_product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='destination_transitions')

    class Meta:
        unique_together = ('user', 'source_product', 'destination_product')  # Combinación única de campos

    def __str__(self):
        return f'{self.user.username} - {self.source_product} -> {self.destination_product}'

    @classmethod
    def register_transition(cls, user, product_origen, product_destino):
        print("jisdsdjiajaij434")
        # Intenta obtener una instancia existente o crear una nueva
        transition, created = cls.objects.get_or_create(
            user=user,
            source_product=product_origen,
            destination_product=product_destino
        )

        # Si la transición ya existe, aumenta el peso

        return transition

class UserViewCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - View Count: {self.view_count}'

class ProductProb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Prob = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user.username} - Producto: {self.Product} - Prob: {self.Prob}'