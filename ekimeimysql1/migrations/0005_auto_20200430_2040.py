# Generated by Django 3.0.2 on 2020-04-30 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeimysql1', '0004_auto_20200430_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.BelongsCategory', verbose_name='所属カテゴリー'),
        ),
        migrations.AlterField(
            model_name='line',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_company', to='ekimeimysql1.Company', verbose_name='事業者コード[id]'),
        ),
        migrations.AlterField(
            model_name='line',
            name='company_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_company_code_old', to='ekimeimysql1.Company', to_field='company_code', verbose_name='事業者コード[code]'),
        ),
        migrations.AlterField(
            model_name='lineservice',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.BelongsCategory', verbose_name='所属カテゴリー'),
        ),
        migrations.AlterField(
            model_name='lineservice',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_service_company', to='ekimeimysql1.Company', verbose_name='事業者コード[id]'),
        ),
        migrations.AlterField(
            model_name='lineservice',
            name='company_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_service_company_code_old', to='ekimeimysql1.Company', to_field='company_code', verbose_name='事業者コード[code]'),
        ),
        migrations.AlterField(
            model_name='part',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Movie', to_field='main_id'),
        ),
        migrations.AlterField(
            model_name='prefecture',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Region', verbose_name='地方'),
        ),
        migrations.AlterField(
            model_name='region',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Country', verbose_name='国'),
        ),
        migrations.AlterField(
            model_name='station',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.NameCategory', verbose_name='名称カテゴリー'),
        ),
        migrations.AlterField(
            model_name='station',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_line', to='ekimeimysql1.Line', verbose_name='路線コード[id]'),
        ),
        migrations.AlterField(
            model_name='station',
            name='line_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_line_code_old', to='ekimeimysql1.Line', to_field='line_code', verbose_name='路線コード[code]'),
        ),
        migrations.AlterField(
            model_name='stationinmovie',
            name='movie_part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Part'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.NameCategory', verbose_name='名称カテゴリー'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='line_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_service_line_service', to='ekimeimysql1.LineService', verbose_name='路線コード(運行系統)[id]'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='line_service_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_service_line_service_code_old', to='ekimeimysql1.LineService', to_field='line_service_code', verbose_name='路線コード(運行系統)[code]'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_service_station', to='ekimeimysql1.Station', verbose_name='駅コード(正式)[id]'),
        ),
        migrations.AlterField(
            model_name='stationservice',
            name='station_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_service_station_code_old', to='ekimeimysql1.Station', to_field='station_code', verbose_name='駅コード(正式)[code]'),
        ),
        migrations.AlterField(
            model_name='stationservicehistory',
            name='line_service_code_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.LineService', to_field='line_service_code', verbose_name='路線コード(運行系統)'),
        ),
        migrations.AlterField(
            model_name='stationservicehistory',
            name='station_service_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.StationService', to_field='station_service_code', verbose_name='駅コード(運行系統)'),
        ),
    ]
