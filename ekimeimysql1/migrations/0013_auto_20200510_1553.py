# Generated by Django 3.0.2 on 2020-05-10 06:53

from django.db import migrations, models
import django.db.models.deletion
import ekimeimysql1.models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimeimysql1', '0012_auto_20200505_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_code',
            field=models.IntegerField(default=ekimeimysql1.models.get_next_company, unique=True, verbose_name='事業者コード'),
        ),
        migrations.CreateModel(
            name='LineInMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.LineService')),
                ('movie_part', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Part')),
            ],
        ),
    ]
