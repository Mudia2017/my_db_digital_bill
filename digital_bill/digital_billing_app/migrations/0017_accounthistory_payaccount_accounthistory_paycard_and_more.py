# Generated by Django 4.2.1 on 2023-10-30 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0016_companyinfo_bonus_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounthistory',
            name='payAccount',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='payCard',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='payMethod',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='payVerify',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
