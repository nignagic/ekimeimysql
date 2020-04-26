from django.db import models

# Create your models here.
class Railway_type(models.Model):
	railway_type_code_2 = models.IntegerField('鉄道種別2コード', default=0)
	railway_type_code = models.IntegerField('鉄道種別コード', default=0)
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	def __str__(self):
		return self.railway_type_name

class Country(models.Model):
	country_code = models.IntegerField(default=0)
	country_name = models.CharField(max_length=200)
	def __str__(self):
		return self.country_name

class Region(models.Model):
	region_code = models.IntegerField(default=0)
	region_name = models.CharField(max_length=200)
	country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE, verbose_name='国')
	def __str__(self):
		return self.region_name

class Prefecture(models.Model):
	pref_code = models.IntegerField(default=0)
	pref_name = models.CharField(max_length=200)
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE, verbose_name='地方')
	def __str__(self):
		return self.pref_name

class Company(models.Model):
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	railway_type_code = models.IntegerField('鉄道種別コード', default=0)
	company_code = models.IntegerField('事業者コード', default=0, unique=True)
	company_name = models.CharField('事業者名', max_length=200, null=True, blank=True)
	company_name_short = models.CharField('事業者名（愛称）', max_length=200, null=True, blank=True)
	company_name_short_2 = models.CharField('事業者名（愛称2）', max_length=200, null=True, blank=True)
	company_name_kana = models.CharField('事業者名読み（かな）', max_length=200, null=True, blank=True)
	company_color = models.CharField('会社色', max_length=100, null=True, blank=True)
	area_code = models.IntegerField('地域', null=True, blank=True)
	sort_by_area = models.CharField('地域ごとの並び順', max_length=100, null=True, blank=True)
	def __str__(self):
		return self.company_name

class Line(models.Model):
	railway_type_name = models.CharField('鉄道種別', max_length=100)
	line_code = models.IntegerField('路線コード', default=0, unique=True)
	line_group_code = models.IntegerField('路線グループコード', default=0)
	line_name_formal = models.CharField('路線名（鉄道要覧）', max_length=200, null=True, blank=True)
	line_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_name_sub = models.CharField('路線区別名', max_length=200, null=True, blank=True)
	company_code = models.ForeignKey(Company, to_field='company_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='事業者コード')
	sort_by_company = models.IntegerField('事業者ごとの並び順', default=0)
	start_station = models.CharField('始点駅', max_length=200, null=True, blank=True)
	end_station = models.CharField('終点駅', max_length=200, null=True, blank=True)
	business_type = models.CharField('第n種事業者', max_length=200, null=True, blank=True)
	is_freight = models.CharField('貨物輸送', max_length=200, null=True, blank=True)
	company_name_2 = models.CharField('事業者名2', max_length=200, null=True, blank=True)
	pref_codes = models.ManyToManyField(Prefecture, blank=True)
	def __str__(self):
		if self.line_name_sub:
			return self.company_code.company_name + " " + self.line_name + "(" + self.line_name_sub + ")"
		else:
			return self.company_code.company_name + " " + self.line_name

class Station(models.Model):
	station_code = models.IntegerField('駅コード', default=0, unique=True)
	station_group_code = models.IntegerField('駅グループコード', default=0)
	station_name = models.CharField('駅名', max_length=200, null=True, blank=True)
	station_name_kana = models.CharField('駅名読み（かな）', max_length=200, null=True, blank=True)
	station_name_en = models.CharField('駅名読み（英語）', max_length=200, null=True, blank=True)
	railway_type = models.CharField('鉄道種別', max_length=100)
	line_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_code = models.ForeignKey(Line, to_field='line_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='路線コード')
	pref_code = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="所在地")
	sort_by_line = models.IntegerField('路線ごとの並び順', null=True, blank=True, default=0)
	pref_cd_old = models.IntegerField('都道府県コード（旧）', null=True, blank=True, default=0)
	post_old = models.CharField('駅郵便番号（旧）', max_length=200, null=True, blank=True)
	add_old = models.CharField('住所（旧）', max_length=200, null=True, blank=True)
	lon_old = models.CharField('経度（旧）', max_length=200, null=True, blank=True)
	lat_old = models.CharField('緯度（旧）', max_length=200, null=True, blank=True)
	open_ymd_old = models.DateField('開業年月日（旧）', max_length=200, null=True, blank=True)
	close_ymd_old = models.DateField('廃止年月日（旧）', max_length=200, null=True, blank=True)

	STATUS = (
		(0, '運用中'),
		(1, '運用前'),
		(2, '廃止')
	)
	e_status_old = models.IntegerField('状態（旧）', null=True, blank=True, choices=STATUS, default=0)
	e_sort_old = models.IntegerField('並び順（旧）', null=True, blank=True, default=0)
	sort = models.IntegerField('並び順', null=True, blank=True, default=0)
	def __str__(self):
		return self.station_name

class LineService(models.Model):
	line_service_code = models.CharField('路線コード(運行系統)', max_length=10, unique=True)
	line_service_name_formal = models.CharField('路線名（鉄道要覧）', max_length=200, null=True, blank=True)
	line_service_name_formal_sub = models.CharField('路線区別名（鉄道要覧）', max_length=200, null=True, blank=True)
	line_code = models.ManyToManyField(Line, blank=True, verbose_name='路線コード(正式)')
	company_name_simple = models.CharField('事業者名(簡易)', max_length=200, null=True, blank=True)
	is_company_name = models.CharField('語頭会社名', max_length=200, null=True, blank=True)
	line_service_name = models.CharField('路線名', max_length=200, null=True, blank=True)
	line_service_name_sub = models.CharField('路線区別名', max_length=200, null=True, blank=True)
	company_code = models.ForeignKey(Company, to_field='company_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='事業者コード')
	sort_by_company = models.IntegerField('事業者ごとの並び順', default=0)
	is_formal = models.CharField('正式区間', max_length=200, null=True, blank=True)
	is_service = models.CharField('運行系統', max_length=200, null=True, blank=True)
	line_color = models.CharField('路線カラー', max_length=100, null=True, blank=True)
	def __str__(self):
		name = ""
		if self.is_company_name:
			name += self.company_name_simple + " "
		name += self.line_service_name
		if self.line_service_name_sub:
			name += "(" + self.line_service_name_sub + ")"
		# name += self.company_name_simple + " " + self.line_service_name_formal
		# if self.line_service_name_formal_sub:
		# 	name += "(" + self.line_service_name_formal_sub + ")"
		if self.is_formal and (self.is_service==""):
			name += "[正式区間]"
		if (self.is_formal=="") and self.is_service:
			name += "[運行系統]"
		return name

class StationService(models.Model):
	station_service_code = models.IntegerField('駅コード(運行系統)', default=0, unique=True)
	station_code = models.ForeignKey(Station, to_field='station_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='駅コード(正式)')
	station_name = models.CharField('駅名', max_length=200, null=True, blank=True)
	line_service_name = models.CharField('路線名(運行系統)', max_length=200, null=True, blank=True)
	line_service_code = models.ForeignKey(LineService, to_field='line_service_code', null=True, blank=True, on_delete=models.CASCADE, verbose_name='路線コード(運行系統)')
	numbering_head = models.CharField('ナンバリング接頭辞', max_length=200, null=True, blank=True)
	numbering_symbol = models.CharField('路線記号', max_length=200, null=True, blank=True)
	numbering_middle = models.CharField('ナンバリングハイフン', max_length=200, null=True, blank=True)
	numbering_number = models.CharField('駅番号', max_length=200, null=True, blank=True)
	sort_by_line_service = models.IntegerField('路線(運行系統)ごとの並び順', null=True, blank=True, default=0)
	station_color = models.CharField('駅カラー', max_length=100, null=True, blank=True)
	def get_numbering(self):
		numbering = self.numbering_head + self.numbering_symbol
		if self.numbering_middle == "space":
			mid = " "
		else:
			mid = self.numbering_middle
		numbering += mid + self.numbering_number + " "
		return numbering

	def get_color(self):
		s = self.station_color
		l = self.line_service_code.line_color
		c = self.line_service_code.company_code.company_color
		if s != "":
			return s
		elif l != "":
			return l
		elif c != "":
			return c
		else:
			return "#06262b"

	def __str__(self):
		name = self.station_name
		if self.station_code.e_status_old == 1:
			name += "[未]"
		elif self.station_code.e_status_old == 2:
			name += "[廃]"
		return name

class MovieCategory(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Creator(models.Model):
	"""人物そのものを表す"""
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class YoutubeChannel(models.Model):
	name = models.CharField(max_length=200)
	channelId = models.CharField(max_length=200, primary_key=True)
	creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, related_name='channel', verbose_name='作者')
	def __str__(self):
		return self.name

class Name(models.Model):
	#名義(合作、単作関わらずこの名前で参加者を記述)
	name = models.CharField(max_length=200)
	creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True, related_name='part_name', verbose_name='作者')
	def __str__(self):
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length=200)
	namerb = models.CharField('アーティスト名カナ', max_length=200, blank=True)
	parent = models.ManyToManyField('self', verbose_name='所属グループ等', blank=True)
	def __str__(self):
		return self.name

class Song(models.Model):
	name = models.CharField('曲名', max_length=200)
	namerb = models.CharField('曲名カナ', max_length=200, blank=True)
	artist = models.ManyToManyField(Artist, blank=True)
	album = models.CharField('アルバム名', max_length=200, blank=True)
	lyrist = models.CharField('作詞者', max_length=200, blank=True)
	composer = models.CharField('作曲者', max_length=200, blank=True)
	tieup = models.CharField('タイアップ等', max_length=200, blank=True)
	description = models.TextField('備考', max_length=500, blank=True)
	parent = models.ManyToManyField('self', verbose_name='原作等', blank=True)
	def __str__(self):
		return self.name

class Vocal(models.Model):
	name = models.CharField('ボーカル名', max_length=200)
	namerb = models.CharField('ボーカル名カナ', max_length=200, blank=True)
	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField('動画タイトル', max_length=200)
	channel = models.ForeignKey(
		YoutubeChannel, on_delete=models.SET_NULL, null=True, verbose_name='投稿チャンネル'
	)
	participant = models.ManyToManyField(
		Name, blank=True, verbose_name='参加者'
	)
	main_id = models.CharField('動画ID', max_length=200, unique=True)
	youtube_id = models.CharField('YouTubeのID', max_length=200, blank=True)
	niconico_id = models.CharField('ニコニコ動画のID', max_length=200, blank=True)
	published_at = models.DateTimeField('投稿日時', blank=True, null=True)
	duration = models.DurationField('動画の長さ', null=True)
	n_view = models.IntegerField('再生回数', default=0, blank=True)
	n_like = models.IntegerField('高評価数', default=0, blank=True)
	n_dislike = models.IntegerField('低評価数', default=0, blank=True)
	n_comment = models.IntegerField('コメント数', default=0, blank=True)
	description = models.TextField('説明', blank=True)

	reg_date = models.DateTimeField('データベース登録日時', blank=True)
	up_date = models.DateTimeField('データベース更新日時', blank=True)

	category = models.ForeignKey(MovieCategory, on_delete=models.SET_NULL, null=True, verbose_name='カテゴリー')
	song = models.ManyToManyField(Song, blank=True, verbose_name='使用楽曲')
	vocal = models.ManyToManyField(Vocal, blank=True, verbose_name='使用ボーカル')
	COLLAB = (
		('S', '単作'),
		('C', '合作')
	)
	is_collab = models.CharField('合作か', max_length=1, choices=COLLAB, default='S')
	parent = models.ManyToManyField('self', verbose_name='親作品', blank=True)
	explanation = models.TextField('補足説明', blank=True)
	def __str__(self):
		return self.title

class Part(models.Model):
	part_num = models.IntegerField()
	part_name_short = models.CharField(max_length=5)
	part_name = models.CharField(max_length=200, blank=True)
	movie = models.ForeignKey(Movie, to_field='main_id', on_delete=models.CASCADE)
	participant = models.ManyToManyField(Name, blank=True, verbose_name='参加名義')
	category = models.ForeignKey(MovieCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='カテゴリー')
	start_time = models.DurationField('開始時間', null=True, blank=True)
	song = models.ManyToManyField(Song, blank=True, verbose_name='使用楽曲')
	song_name = models.CharField(max_length=200, blank=True)
	vocal = models.ManyToManyField(Vocal, blank=True, verbose_name='使用ボーカル')
	explanation = models.TextField('説明', blank=True)
	def __str__(self):
		return self.part_name + " [" + self.movie.title + "]"

class StationInMovie(models.Model):
	id_in_part = models.IntegerField()
	movie_part = models.ForeignKey(Part, on_delete=models.CASCADE)
	station_service_code = models.ForeignKey(StationService, to_field='station_service_code', on_delete=models.CASCADE)
	station_name = models.CharField(max_length=200)
	non_line = models.BooleanField('路線不定', default=False)
	back_rel = models.IntegerField('前駅との関係', default=1)
	is_sung = models.BooleanField('歌唱されているか(同じ駅が重複している場合は偽)', default=True)
	def __str__(self):
		return self.station_name