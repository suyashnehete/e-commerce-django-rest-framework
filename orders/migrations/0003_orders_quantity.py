# Generated by Django 3.2.3 on 2021-05-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orders_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
