# Generated by Django 5.1.4 on 2024-12-21 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_loja_nome_usuario_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
