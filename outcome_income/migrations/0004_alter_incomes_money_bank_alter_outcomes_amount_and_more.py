# Generated by Django 4.0.5 on 2022-06-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outcome_income', '0003_remove_incomes_bank_remove_outcomes_bank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomes',
            name='money_bank',
            field=models.CharField(choices=[('Money', 'Money'), ('Bank', 'Bank')], max_length=32),
        ),
        migrations.AlterField(
            model_name='outcomes',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='outcomes',
            name='money_bank',
            field=models.CharField(choices=[('Money', 'Money'), ('Bank', 'Bank')], max_length=32),
        ),
    ]
