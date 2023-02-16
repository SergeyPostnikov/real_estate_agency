# Generated by Django 2.2.24 on 2023-02-14 17:14

from django.db import migrations


def separate_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    
    for flat in flats.iterator():        
        Owner.objects.get_or_create(
            owner_name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(separate_owner),
    ]
