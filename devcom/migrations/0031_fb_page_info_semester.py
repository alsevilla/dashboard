# Generated by Django 3.1.2 on 2021-03-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0030_auto_20210309_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='fb_page_info',
            name='semester',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
