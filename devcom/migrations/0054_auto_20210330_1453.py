# Generated by Django 3.1.2 on 2021-03-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0053_auto_20210330_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kp_input_stock',
            name='printing_press',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
