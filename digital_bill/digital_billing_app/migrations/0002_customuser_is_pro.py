# Generated by Django 4.2.1 on 2023-07-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_pro',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
