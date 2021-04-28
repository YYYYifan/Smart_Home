# Generated by Django 3.1.7 on 2021-04-19 00:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True)),
                ('group', models.CharField(choices=[('water', '水系统'), ('wind', '通风系统'), ('TEST', 'TEST')], default='TEST', max_length=32)),
                ('comment', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]