# Generated by Django 3.2.7 on 2022-10-31 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
