# Generated by Django 3.0.2 on 2020-04-29 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeimysql1', '0011_auto_20200429_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationservice',
            name='station_service_group_code',
        ),
    ]
