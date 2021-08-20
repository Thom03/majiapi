# Generated by Django 2.1.5 on 2021-08-18 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_unitcharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitcharge',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='unitcharge', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]