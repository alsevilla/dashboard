# Generated by Django 3.1.2 on 2021-02-19 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0002_auto_20210219_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kp_input_stock',
            old_name='kp_id',
            new_name='kp',
        ),
    ]
