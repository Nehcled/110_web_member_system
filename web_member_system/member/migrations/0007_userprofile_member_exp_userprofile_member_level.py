# Generated by Django 4.0 on 2021-12-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_remove_userprofile_uniqueid_userprofile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='member_exp',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member_level',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
        ),
    ]