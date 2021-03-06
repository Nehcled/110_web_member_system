# Generated by Django 3.2.9 on 2021-12-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='job',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='head_shot'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skill',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
