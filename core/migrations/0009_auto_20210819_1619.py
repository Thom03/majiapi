# Generated by Django 2.1.5 on 2021-08-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210819_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreading',
            name='consumption',
            field=models.FloatField(blank=True, max_length=14),
        ),
    ]
