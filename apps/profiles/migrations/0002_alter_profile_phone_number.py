# Generated by Django 3.2.7 on 2022-10-26 11:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+265998108842', max_length=30, region=None, verbose_name='Phone Number'),
        ),
    ]