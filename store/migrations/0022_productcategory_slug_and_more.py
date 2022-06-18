# Generated by Django 4.0.5 on 2022-06-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_productinstock_currency_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='productCategory',
            field=models.CharField(max_length=64),
        ),
    ]