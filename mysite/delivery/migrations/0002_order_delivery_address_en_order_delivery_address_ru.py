# Generated by Django 5.1.3 on 2024-11-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
