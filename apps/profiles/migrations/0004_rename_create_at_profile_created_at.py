# Generated by Django 3.2.7 on 2022-10-31 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='create_at',
            new_name='created_at',
        ),
    ]