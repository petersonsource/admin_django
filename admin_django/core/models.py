from django.db import models

# Create your models here.

class Loja(models.Model):
    account  = models.CharField(max_length=100)
    appkey  = models.CharField(max_length=100)
    apptoken  = models.CharField(max_length=100)

    def __str__(self):
        return self.account

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField(null=True)
    loja = models.ForeignKey('Loja', on_delete=models.CASCADE, related_name='perfis')

    class Meta:
        unique_together = ('loja','codigo')

    def __str__(self):
        return f'{self.nome}/{self.loja.account}/{self.codigo}'


class Usuario(models.Model):
    user_id = models.CharField(max_length=100,null=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class UsuarioPerfil(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='perfis')
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='usuarios')

    class Meta:
        unique_together = ('usuario','perfil')

    def __str__(self):
        return f'{self.usuario.nome}/{self.perfil.nome}/{self.perfil.loja.account}'
