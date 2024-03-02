# Generated by Django 4.2.1 on 2023-09-09 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0012_alter_accounthistory_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounthistory',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounthistory',
            name='transaction_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]