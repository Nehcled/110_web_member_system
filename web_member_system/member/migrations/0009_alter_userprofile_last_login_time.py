# Generated by Django 3.2.9 on 2021-12-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_userprofile_last_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_login_time',
            field=models.DateField(null=True),
        ),
    ]
