from django.db import models
from django.contrib.auth.models import User
from CarritoApp.models import Producto  # Importa el modelo de Producto desde tu aplicación

class Transition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='link_transitions')
    source_product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='source_transitions')
    destination_product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='destination_transitions')
    peso = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'product_origen', 'product_destino')  # Combinación única de campos

    def __str__(self):
        return f'{self.user.username} - {self.product_origen} -> {self.product_destino}'

    @classmethod
    def register_transition(cls, user, product_origen, product_destino):
        # Intenta obtener una instancia existente o crear una nueva
        transition, created = cls.objects.get_or_create(
            user=user,
            product_origen=product_origen,
            product_destino=product_destino
        )

        # Si la transición ya existe, aumenta el peso
        if not created:
            transition.peso += 1
            transition.save()

        return transition

