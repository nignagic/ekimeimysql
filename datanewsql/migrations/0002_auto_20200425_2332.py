# Generated by Django 3.0.2 on 2020-04-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datanewsql', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='area_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='地域'),
        ),
    ]
