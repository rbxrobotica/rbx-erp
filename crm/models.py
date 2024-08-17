from django.db import models

ETAPAS_FUNIL = {
    'Descoberta': 'Discovery',
    'Consideração': 'Consideration',
    'Decisão': 'Decision',
    'Pós-Venda': 'Post-Sale',
}

class Origem(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Lead(models.Model):
    origem = models.ForeignKey(Origem, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_captura = models.DateField()
    detalhes = models.TextField()

class Funil(models.Model):
    nome = models.CharField(max_length=100)
    leads = models.ManyToManyField(Lead)

class EtapaFunil(models.Model):
    funil = models.ForeignKey(Funil, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, choices=ETAPAS_FUNIL.items())
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    detalhes = models.TextField()
