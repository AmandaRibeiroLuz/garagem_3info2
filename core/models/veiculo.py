from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2,default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    
    def __str__(self):
        return f"({self.id}) {(self.modelo or "")} - {(self.cor) or ""} - {(self.ano)}."
    
    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'