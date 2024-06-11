# Generated by Django 5.0.6 on 2024-06-05 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('discount', models.IntegerField()),
                ('min_order', models.IntegerField(blank=True, null=True)),
                ('usage_limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_at', models.DateTimeField(auto_now=True)),
                ('usage_count', models.IntegerField(default=0)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupons.coupon')),
            ],
        ),
    ]
