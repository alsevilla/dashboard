# Generated by Django 3.1.2 on 2021-03-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0011_auto_20210225_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='kp_distribute',
            name='Date',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
