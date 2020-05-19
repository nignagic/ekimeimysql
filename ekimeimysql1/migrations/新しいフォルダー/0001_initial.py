# Generated by Django 3.0.2 on 2020-02-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ManyToManyField(blank=True, related_name='_artist_parent_+', to='ekimeimysql1.Artist', verbose_name='所属グループ等')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('railway_type_code', models.IntegerField(default=0, verbose_name='鉄道種別コード')),
                ('company_code', models.IntegerField(default=0, unique=True, verbose_name='事業者コード')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名')),
                ('company_name_short', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名（愛称）')),
                ('company_name_short_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名（愛称2）')),
                ('company_name_kana', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名読み（かな）')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('line_code', models.IntegerField(default=0, unique=True, verbose_name='路線コード')),
                ('line_group_code', models.IntegerField(default=0, verbose_name='路線グループコード')),
                ('line_name_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名（鉄道要覧）')),
                ('line_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('line_name_sub', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線区別名')),
                ('sort_by_company', models.IntegerField(default=0, verbose_name='事業者ごとの並び順')),
                ('start_station', models.CharField(blank=True, max_length=200, null=True, verbose_name='始点駅')),
                ('end_station', models.CharField(blank=True, max_length=200, null=True, verbose_name='終点駅')),
                ('business_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='第n種事業者')),
                ('is_freight', models.CharField(blank=True, max_length=200, null=True, verbose_name='貨物輸送')),
                ('company_name_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名2')),
                ('company_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Company', to_field='company_code', verbose_name='事業者コード')),
            ],
        ),
        migrations.CreateModel(
            name='LineService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_service_code', models.CharField(max_length=10, unique=True, verbose_name='路線コード(運行系統)')),
                ('line_service_name_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名（鉄道要覧）')),
                ('line_service_name_formal_sub', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線区別名（鉄道要覧）')),
                ('company_name_simple', models.CharField(blank=True, max_length=200, null=True, verbose_name='事業者名(簡易)')),
                ('is_company_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='語頭会社名')),
                ('line_service_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('line_service_name_sub', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線区別名')),
                ('sort_by_company', models.IntegerField(default=0, verbose_name='事業者ごとの並び順')),
                ('is_formal', models.CharField(blank=True, max_length=200, null=True, verbose_name='正式区間')),
                ('is_service', models.CharField(blank=True, max_length=200, null=True, verbose_name='運行系統')),
                ('company_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Company', to_field='company_code', verbose_name='事業者コード')),
                ('line_code', models.ManyToManyField(blank=True, to='ekimeimysql1.Line', verbose_name='路線コード(正式)')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='動画タイトル')),
                ('main_id', models.CharField(max_length=200, unique=True, verbose_name='動画ID')),
                ('youtube_id', models.CharField(blank=True, max_length=200, verbose_name='YouTubeのID')),
                ('niconico_id', models.CharField(blank=True, max_length=200, verbose_name='ニコニコ動画のID')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='投稿日時')),
                ('duration', models.DurationField(null=True, verbose_name='動画の長さ')),
                ('n_view', models.IntegerField(blank=True, default=0, verbose_name='再生回数')),
                ('n_like', models.IntegerField(blank=True, default=0, verbose_name='高評価数')),
                ('n_dislike', models.IntegerField(blank=True, default=0, verbose_name='低評価数')),
                ('n_comment', models.IntegerField(blank=True, default=0, verbose_name='コメント数')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('reg_date', models.DateTimeField(blank=True, verbose_name='データベース登録日時')),
                ('is_collab', models.CharField(choices=[('S', '単作'), ('C', '合作')], default='S', max_length=1, verbose_name='合作か')),
                ('explanation', models.TextField(blank=True, verbose_name='補足説明')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Category', verbose_name='カテゴリー')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part_name', to='ekimeimysql1.Creator', verbose_name='名義')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_num', models.IntegerField()),
                ('part_name_short', models.CharField(max_length=5)),
                ('part_name', models.CharField(blank=True, max_length=200)),
                ('start_time', models.DurationField(blank=True, null=True, verbose_name='開始時間')),
                ('explanation', models.TextField(blank=True, verbose_name='説明')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.Category', verbose_name='カテゴリー')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Movie', to_field='main_id')),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_code', models.IntegerField(default=0, unique=True)),
                ('pref_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Railway_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_type_code_2', models.IntegerField(default=0, verbose_name='鉄道種別2コード')),
                ('railway_type_code', models.IntegerField(default=0, verbose_name='鉄道種別コード')),
                ('railway_type_name', models.CharField(max_length=100, verbose_name='鉄道種別')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.IntegerField(default=0, unique=True, verbose_name='駅コード')),
                ('station_group_code', models.IntegerField(default=0, verbose_name='駅グループコード')),
                ('station_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名')),
                ('station_name_kana', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名読み（かな）')),
                ('station_name_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名読み（英語）')),
                ('railway_type', models.CharField(max_length=100, verbose_name='鉄道種別')),
                ('line_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名')),
                ('sort_by_line', models.IntegerField(blank=True, default=0, null=True, verbose_name='路線ごとの並び順')),
                ('post_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅郵便番号（旧）')),
                ('add_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='住所（旧）')),
                ('lon_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='経度（旧）')),
                ('lat_old', models.CharField(blank=True, max_length=200, null=True, verbose_name='緯度（旧）')),
                ('open_ymd_old', models.DateField(blank=True, max_length=200, null=True, verbose_name='開業年月日（旧）')),
                ('close_ymd_old', models.DateField(blank=True, max_length=200, null=True, verbose_name='廃止年月日（旧）')),
                ('e_status_old', models.IntegerField(blank=True, choices=[(0, '運用中'), (1, '運用前'), (2, '廃止')], default=0, null=True, verbose_name='状態（旧）')),
                ('e_sort_old', models.IntegerField(blank=True, default=0, null=True, verbose_name='並び順（旧）')),
                ('sort', models.IntegerField(blank=True, default=0, null=True, verbose_name='並び順')),
                ('line_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Line', to_field='line_code', verbose_name='路線コード')),
                ('pref_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Prefecture', to_field='pref_code', verbose_name='都道府県')),
            ],
        ),
        migrations.CreateModel(
            name='Vocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ボーカル名')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('channelId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to='ekimeimysql1.Creator', verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='StationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_service_code', models.IntegerField(default=0, unique=True, verbose_name='駅コード(運行系統)')),
                ('station_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅名')),
                ('line_service_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線名(運行系統)')),
                ('numbering_symbol', models.CharField(blank=True, max_length=200, null=True, verbose_name='路線記号')),
                ('numbering_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='駅番号')),
                ('sort_by_line_service', models.IntegerField(blank=True, default=0, null=True, verbose_name='路線(運行系統)ごとの並び順')),
                ('line_service_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.LineService', to_field='line_service_code', verbose_name='路線コード(運行系統)')),
                ('station_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Station', to_field='station_code', verbose_name='駅コード(正式)')),
            ],
        ),
        migrations.CreateModel(
            name='StationInMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_movie', models.IntegerField()),
                ('station_name', models.CharField(max_length=200)),
                ('non_line', models.BooleanField(default=False, verbose_name='路線不定')),
                ('back_rel', models.IntegerField(default=1, verbose_name='前駅との関係')),
                ('movie_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.Part')),
                ('station_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekimeimysql1.StationService', to_field='station_service_code')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='曲名')),
                ('namerb', models.CharField(blank=True, max_length=200, verbose_name='曲名カナ')),
                ('album', models.CharField(blank=True, max_length=200, verbose_name='アルバム名')),
                ('lyrist', models.CharField(blank=True, max_length=200, verbose_name='作詞者')),
                ('composer', models.CharField(blank=True, max_length=200, verbose_name='作曲者')),
                ('tieup', models.CharField(blank=True, max_length=200, verbose_name='タイアップ等')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='備考')),
                ('artist', models.ManyToManyField(blank=True, to='ekimeimysql1.Artist')),
                ('parent', models.ManyToManyField(blank=True, related_name='_song_parent_+', to='ekimeimysql1.Song', verbose_name='原作等')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='part_song',
            field=models.ManyToManyField(blank=True, related_name='part_songs', to='ekimeimysql1.Song', verbose_name='使用楽曲(一部)'),
        ),
        migrations.AddField(
            model_name='part',
            name='part_vocal',
            field=models.ManyToManyField(blank=True, related_name='part_vocals', to='ekimeimysql1.Vocal', verbose_name='使用ボーカル(一部)'),
        ),
        migrations.AddField(
            model_name='part',
            name='participant',
            field=models.ManyToManyField(blank=True, to='ekimeimysql1.Name', verbose_name='参加名義'),
        ),
        migrations.AddField(
            model_name='movie',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimeimysql1.YoutubeChannel', verbose_name='投稿チャンネル'),
        ),
        migrations.AddField(
            model_name='movie',
            name='parent',
            field=models.ManyToManyField(blank=True, related_name='_movie_parent_+', to='ekimeimysql1.Movie', verbose_name='親作品'),
        ),
        migrations.AddField(
            model_name='movie',
            name='participant',
            field=models.ManyToManyField(blank=True, to='ekimeimysql1.Name', verbose_name='参加者'),
        ),
        migrations.AddField(
            model_name='movie',
            name='song',
            field=models.ManyToManyField(blank=True, related_name='entire_songs_in_movie', to='ekimeimysql1.Song', verbose_name='使用楽曲(作品全体)'),
        ),
        migrations.AddField(
            model_name='movie',
            name='vocal',
            field=models.ManyToManyField(blank=True, related_name='entire_vocals', to='ekimeimysql1.Vocal', verbose_name='使用ボーカル(作品全体)'),
        ),
        migrations.AddField(
            model_name='lineservice',
            name='pref_codes',
            field=models.ManyToManyField(blank=True, to='ekimeimysql1.Prefecture'),
        ),
        migrations.AddField(
            model_name='line',
            name='pref_codes',
            field=models.ManyToManyField(blank=True, to='ekimeimysql1.Prefecture'),
        ),
    ]
