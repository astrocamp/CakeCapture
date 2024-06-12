# Generated by Django 5.0.6 on 2024-06-12 03:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coupons', '0001_initial'),
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercoupon',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usercoupons_coupons', to='orders.order'),
        ),
        migrations.AddField(
            model_name='usercoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coupon',
            name='users',
            field=models.ManyToManyField(related_name='coupons', through='coupons.UserCoupon', to=settings.AUTH_USER_MODEL),
        ),
    ]
