# Generated by Django 5.0.6 on 2024-05-12 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_newuser_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='county',
            new_name='country',
        ),
    ]
