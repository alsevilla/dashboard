# Generated by Django 3.1.2 on 2021-05-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0068_auto_20210503_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kp_input',
            name='date_record',
            field=models.DateTimeField(),
        ),
    ]
