# Generated by Django 3.1.2 on 2021-02-24 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0007_auto_20210224_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kp_distribute',
            name='kp',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='devcom.kp_input'),
        ),
    ]
