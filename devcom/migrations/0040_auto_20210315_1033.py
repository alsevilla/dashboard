# Generated by Django 3.1.2 on 2021-03-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0039_auto_20210315_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr_visitor',
            name='quarter',
            field=models.CharField(choices=[('1Q', '1st Quarter'), ('2Q', '2nd Quarter'), ('3Q', '3rd Quarter'), ('4Q', '4th Quarter')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pw_visitor',
            name='quarter',
            field=models.CharField(choices=[('1Q', '1st Quarter'), ('2Q', '2nd Quarter'), ('3Q', '3rd Quarter'), ('4Q', '4th Quarter')], max_length=60, null=True),
        ),
    ]
