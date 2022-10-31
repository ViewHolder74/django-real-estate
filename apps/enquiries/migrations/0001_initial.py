# Generated by Django 3.2.7 on 2022-10-31 19:23

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Your Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+265998108842', max_length=30, region=None, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]
