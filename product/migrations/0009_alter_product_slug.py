# Generated by Django 4.0 on 2022-04-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
