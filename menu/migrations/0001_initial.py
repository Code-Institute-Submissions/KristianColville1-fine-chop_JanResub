# Generated by Django 3.2.16 on 2022-11-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_code', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('A', 'Starters'), ('B', 'Mains'), ('C', 'Noodles'), ('D', 'Rices'), ('E', 'Wok'), ('F', 'Curries'), ('G', 'Soups'), ('H', 'Vegan'), ('I', 'Salads'), ('J', 'Kids Menu'), ('K', 'Drinks')], max_length=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Not Serving'), (1, 'Serving')], default=1)),
            ],
            options={
                'verbose_name_plural': 'Food Items',
                'abstract': False,
            },
        ),
    ]