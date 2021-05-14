# Generated by Django 3.1.2 on 2021-03-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcom', '0033_fb_post_data_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pr_visitor',
            name='sno',
        ),
        migrations.RemoveField(
            model_name='pr_visitor',
            name='syes',
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='desktop',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='mobile',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='nosex',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='organic',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='pageviews',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='redirect',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='referral',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='social',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pr_visitor',
            name='tablet',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
