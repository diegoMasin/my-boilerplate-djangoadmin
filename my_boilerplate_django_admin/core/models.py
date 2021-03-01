from django.db import models


class Article(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)

    class Meta:
        ordering = ("titulo",)
        verbose_name = "artigo"
        verbose_name_plural = "artigos"

    def __str__(self):
        return f"{self.titulo} - {self.descricao}"
