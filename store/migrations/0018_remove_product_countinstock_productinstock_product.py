# Generated by Django 4.0.5 on 2022-06-08 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_productinstock_remove_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='countInStock',
        ),
        migrations.AddField(
            model_name='productinstock',
            name='product',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
