# Generated by Django 3.2.16 on 2022-11-10 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(max_length=320, unique=True)),
                ('default_phone_number', models.CharField(blank=True, max_length=22, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=90, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=90, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=55, null=True)),
                ('default_county', models.CharField(blank=True, max_length=100, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=18, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]