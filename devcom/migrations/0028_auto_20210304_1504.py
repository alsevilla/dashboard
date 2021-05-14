# Generated by Django 3.1.2 on 2021-03-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0027_auto_20210304_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ptc',
            old_name='PTCfemale',
            new_name='female',
        ),
        migrations.RenameField(
            model_name='ptc',
            old_name='PTCmale',
            new_name='male',
        ),
        migrations.RemoveField(
            model_name='ptc',
            name='RCEFfemale',
        ),
        migrations.RemoveField(
            model_name='ptc',
            name='RCEFmale',
        ),
        migrations.RemoveField(
            model_name='ptc',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ptc',
            name='datefortable',
        ),
        migrations.AddField(
            model_name='ptc',
            name='month',
            field=models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='ptc',
            name='year',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
