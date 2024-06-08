# Generated by Django 5.0.6 on 2024-06-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('payment_fail', 'Payment Fail'), ('waiting_for_shipment', 'Waiting for shipment'), ('transporting', 'Transporting'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('waiting_for_check', 'Waiting for check')], default='waiting_for_check', max_length=100),
        ),
    ]
