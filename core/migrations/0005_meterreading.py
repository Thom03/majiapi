# Generated by Django 2.1.5 on 2021-08-19 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210819_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_reading', models.FloatField(blank=True, max_length=14)),
                ('current_reading', models.FloatField(blank=True, max_length=14)),
                ('consumption', models.FloatField(editable=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meterreading', to='core.Customer')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': ('-created',),
            },
        ),
    ]
