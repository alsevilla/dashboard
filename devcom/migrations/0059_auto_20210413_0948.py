# Generated by Django 3.1.2 on 2021-04-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0058_kp_input_monthfortable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kp_input',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
