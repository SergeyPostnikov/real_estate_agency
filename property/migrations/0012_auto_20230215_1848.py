# Generated by Django 2.2.24 on 2023-02-15 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230215_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]