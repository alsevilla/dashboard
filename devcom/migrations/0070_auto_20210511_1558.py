# Generated by Django 3.1.2 on 2021-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0069_auto_20210511_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kp_input_stock',
            name='date_recorded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
