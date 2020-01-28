from django.db import models


class Documentos(models.Model):

    CPFOUCNPJ = models.CharField(max_length=255, null=False)
    NOME = models.CharField(max_length=255, null=False)
    CELULAR = models.CharField(max_length=255, null=False)
    RESULTADOCONSULTAS = models.CharField(null=False)
    def __str__(self):
        return "{} - {}".format(self.CPFOUCNPJ, self.NOME, self.CELULAR, self.RESULTADOCONSULTAS)