# Generated by Django 4.2.1 on 2023-10-31 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0018_rename_payaccount_accounthistory_bank_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_cus', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('referred_cus_initial_deposit', models.FloatField(default=0, max_length=15)),
                ('is_payment_verified', models.BooleanField(default=False)),
                ('percentage_rate', models.FloatField(default=0, max_length=5)),
                ('bonus_amt', models.FloatField(default=0, max_length=15)),
                ('referral_process', models.CharField(blank=True, default='', max_length=200)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('referral_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
