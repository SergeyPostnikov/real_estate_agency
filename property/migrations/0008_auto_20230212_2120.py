# Generated by Django 2.2.24 on 2023-02-12 18:20

from django.db import migrations
import phonenumbers


def validate_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(pure_phone):
            flat.owner_pure_phone = pure_phone
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(validate_phones),
    ]
