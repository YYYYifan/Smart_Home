# Generated by Django 3.1.7 on 2021-04-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(choices=[('online', '在线'), ('offline', '离线'), ('warning', '连接不稳定')], default='warning', max_length=32),
        ),
    ]