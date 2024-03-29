# Generated by Django 4.2.1 on 2023-08-19 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_billing_app', '0004_alter_customuser_is_deactivateacct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_deactivateAcct',
        ),
        migrations.AddField(
            model_name='customuser',
            name='airtime_default_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='customuser',
            name='cable_iuc_default',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='customuser',
            name='data_default_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='debit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='customuser',
            name='internet_default_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='meter_default_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.CharField(blank=True, max_length=200, null=True)),
                ('service_fee', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('data_amt', models.CharField(blank=True, max_length=200, null=True)),
                ('percent_discount', models.CharField(blank=True, max_length=200, null=True)),
                ('amt_after_discount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('subscription_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital_billing_app.datasubscription')),
            ],
        ),
    ]
