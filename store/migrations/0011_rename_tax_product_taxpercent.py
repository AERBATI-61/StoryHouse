# Generated by Django 3.2.6 on 2022-06-08 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220608_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tax',
            new_name='taxPercent',
        ),
    ]
