# Generated by Django 4.2.1 on 2023-08-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0007_rename_customer_id_accounthistory_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounthistory',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
