# Generated by Django 3.1.2 on 2021-03-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0032_auto_20210309_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='fb_post_data',
            name='semester',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
