# Generated by Django 4.0.5 on 2022-06-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_seller_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]