# Generated by Django 3.2.9 on 2021-12-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_userprofile_last_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='head_shot',
            field=models.CharField(default='template_of_head_shot.png', max_length=100),
        ),
    ]
