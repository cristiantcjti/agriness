# Generated by Django 3.1.8 on 2021-04-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210422_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(blank=True, choices=[(0, 'disponível'), (1, 'emprestado')], null=True),
        ),
    ]