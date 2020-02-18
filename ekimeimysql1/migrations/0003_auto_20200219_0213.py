# Generated by Django 3.0.2 on 2020-02-18 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeimysql1', '0002_auto_20200219_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationinmovie',
            name='station_cd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old', to='ekimeimysql1.StationService', to_field='station_service_code'),
        ),
        migrations.AlterField(
            model_name='stationinmovie',
            name='station_service_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='駅名', to='ekimeimysql1.StationService', to_field='station_service_code'),
        ),
    ]