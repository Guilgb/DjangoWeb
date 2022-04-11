from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(datetime.now, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_receita
