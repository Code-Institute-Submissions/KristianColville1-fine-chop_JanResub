# Generated by Django 3.2.16 on 2023-01-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20230102_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='contents',
            field=models.TextField(),
        ),
    ]
