# Generated by Django 2.1.5 on 2021-08-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210819_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreading',
            name='consumption',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
