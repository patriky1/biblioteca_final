# Generated by Django 4.1.7 on 2023-03-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_livros_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='capa_livro'),
        ),
    ]
