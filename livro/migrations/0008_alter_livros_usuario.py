# Generated by Django 4.1.7 on 2023-03-13 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0007_remove_livros_usuario_livros_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
