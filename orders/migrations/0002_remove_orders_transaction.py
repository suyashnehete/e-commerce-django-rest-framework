# Generated by Django 3.2.3 on 2021-05-28 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='transaction',
        ),
    ]