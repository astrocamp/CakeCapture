# Generated by Django 5.0.6 on 2024-06-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordermethod_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermethod',
            name='payment_method',
            field=models.CharField(choices=[('信用卡', '信用卡'), ('LINE_PAY', 'LINE PAY'), ('ATM 轉帳付款', 'ATM 轉帳付款')], default='信用卡', max_length=20),
        ),
    ]
