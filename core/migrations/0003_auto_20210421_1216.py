# Generated by Django 3.1.8 on 2021-04-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210421_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreservations',
            name='date_lent',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookreservations',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
    ]
