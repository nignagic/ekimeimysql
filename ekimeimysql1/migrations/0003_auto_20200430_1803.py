# Generated by Django 3.0.2 on 2020-04-30 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeimysql1', '0002_stationservice_station_service_group_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationservice',
            name='line_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='line_service', to='ekimeimysql1.LineService', verbose_name='路線コード(運行系統)[id]'),
        ),
        migrations.AddField(
            model_name='stationservice',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='station', to='ekimeimysql1.Station', verbose_name='駅コード(正式)[id]'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='line_service_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='line_service_code_old', to='ekimeimysql1.LineService', to_field='line_service_code', verbose_name='路線コード(運行系統)[code]'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='station_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='station_code_old', to='ekimeimysql1.Station', to_field='station_code', verbose_name='駅コード(正式)[code]'),
        ),
    ]
