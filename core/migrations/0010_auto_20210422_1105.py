# Generated by Django 3.1.8 on 2021-04-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210422_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(default='disponível', max_length=15),
        ),
    ]
