# Generated by Django 3.1.2 on 2021-03-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0034_auto_20210311_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr_visitor',
            name='noage',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
