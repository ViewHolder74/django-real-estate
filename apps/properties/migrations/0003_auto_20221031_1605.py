# Generated by Django 3.2.7 on 2022-10-31 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='taxt',
            new_name='tax',
        ),
        migrations.RenameField(
            model_name='propertyviews',
            old_name='create_at',
            new_name='created_at',
        ),
    ]