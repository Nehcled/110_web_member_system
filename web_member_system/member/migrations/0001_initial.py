# Generated by Django 4.0 on 2021-12-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(max_length=2000, null=True)),
                ('skill', models.TextField(max_length=2000, null=True)),
                ('job', models.TextField(max_length=2000, null=True)),
                ('cel', models.CharField(max_length=100, null=True)),
                ('tel', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
