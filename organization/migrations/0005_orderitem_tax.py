# Generated by Django 3.2.6 on 2022-06-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20220608_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='tax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
