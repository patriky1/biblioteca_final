# Generated by Django 4.1.7 on 2023-03-18 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_remove_turma_nome_turma_turma_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='turma',
        ),
    ]
