from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import Movie, Part, StationInMovie, Company, Line, Station, LineService, StationService

from django.contrib.auth.forms import (
	AuthenticationForm
)

class LoginForm(AuthenticationForm):
	"""ログインフォーム"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['placeholder'] = field.label

class MovieRegisterForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_comment', 'description', 'reg_date')
		widgets = {
			'title': forms.HiddenInput(attrs={
				'class': 'title',
			}),
			'channel': forms.HiddenInput(attrs={
				'id': 'channel',
			}),
			'main_id': forms.HiddenInput(attrs={
				'class': 'main_id',
			}),
			'youtube_id': forms.HiddenInput(attrs={
				'class': 'youtube_id',
			}),
			'niconico_id': forms.HiddenInput(attrs={
				'class': 'niconico_id',
			}),
			'published_at': forms.HiddenInput(attrs={
				'class': 'published_at',
			}),
			'duration': forms.HiddenInput(attrs={
				'class': 'duration',
			}),
			'n_view': forms.HiddenInput(attrs={
				'class': 'n_view',
			}),
			'n_like': forms.HiddenInput(attrs={
				'class': 'n_like',
			}),
			'n_dislike': forms.HiddenInput(attrs={
				'class': 'n_dislike',
			}),
			'n_comment': forms.HiddenInput(attrs={
				'class': 'n_comment',
			}),
			'description': forms.HiddenInput(attrs={
				'class': 'description',
			}),
			'reg_date': forms.HiddenInput(attrs={
				'class': 'reg_date',
			}),
		}
		labels = {
			'title': '',
			'channel': '',
			'main_id': '',
			'youtube_id': '',
			'niconico_id': '',
			'published_at': '',
			'duration': '',
			'n_view': '',
			'n_like': '',
			'n_dislike': '',
			'n_comment': '',
			'description': '',
			'reg_date': '',
		}

class MovieUpdateForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_dislike', 'n_comment', 'description', 'reg_date', 'song', 'vocal', 'is_collab', 'parent', 'explanation')
		widgets = {
			'title': forms.HiddenInput(attrs={
				'class': 'title',
			}),
			'channel': forms.HiddenInput(attrs={
				'id': 'channel',
			}),
			'main_id': forms.HiddenInput(attrs={
				'class': 'main_id',
			}),
			'youtube_id': forms.HiddenInput(attrs={
				'class': 'youtube_id',
			}),
			'niconico_id': forms.HiddenInput(attrs={
				'class': 'niconico_id',
			}),
			'published_at': forms.HiddenInput(attrs={
				'class': 'published_at',
			}),
			'duration': forms.HiddenInput(attrs={
				'class': 'duration',
			}),
			'n_view': forms.HiddenInput(attrs={
				'class': 'n_view',
			}),
			'n_like': forms.HiddenInput(attrs={
				'class': 'n_like',
			}),
			'n_dislike': forms.HiddenInput(attrs={
				'class': 'n_dislike',
			}),
			'n_comment': forms.HiddenInput(attrs={
				'class': 'n_comment',
			}),
			'description': forms.HiddenInput(attrs={
				'class': 'description',
			}),
			'reg_date': forms.HiddenInput(attrs={
				'class': 'reg_date',
			}),
		}

class PartEditFormforinlineold(forms.ModelForm):
	class Meta:
		model = Part
		fields = ('part_num', 'part_name_short', 'part_name', 'movie', 'participant', 'category', 'start_time', 'part_song', 'part_vocal', 'explanation')
		widgets = {
			'part_num': forms.HiddenInput(attrs={
				'class': 'part_num',
			}),
			'part_name_short': forms.HiddenInput(attrs={
				'class': 'part_name_short',
			}),
			'part_name': forms.HiddenInput(attrs={
				'class': 'part_name',
			}),
			'movie': forms.HiddenInput(attrs={
				'class': 'movie',
			}),
			'participant': forms.SelectMultiple(attrs={
				'class': 'participant',
			}),
			'category': forms.Select(attrs={
				'class': 'category',
			}),
			'start_time': forms.HiddenInput(attrs={
				'class': 'start_time',
			}),
			'part_song': forms.SelectMultiple(attrs={
				'class': 'part_song',
			}),
			'part_vocal': forms.SelectMultiple(attrs={
				'class': 'part_vocal',
			}),
			'explanation': forms.HiddenInput(attrs={
				'class': 'explanation',
			}),
		}

class PartEditFormforinline(forms.ModelForm):
	class Meta:
		model = Part
		fields = ('part_num', 'part_name_short', 'part_name', 'movie', 'participant', 'category', 'start_time', 'part_song', 'part_vocal', 'explanation')
		widgets = {
			'part_num': forms.HiddenInput(attrs={
				'class': 'part_num',
			}),
			'part_name_short': forms.TextInput(attrs={
				'class': 'part_name_short',
			}),
			'part_name': forms.TextInput(attrs={
				'class': 'part_name',
			}),
			'movie': forms.HiddenInput(attrs={
				'class': 'movie',
			}),
			'participant': forms.MultipleHiddenInput(attrs={
				'class': 'participant',
			}),
			'category': forms.Select(attrs={
				'class': 'category',
			}),
			'start_time': forms.TextInput(attrs={
				'class': 'start_time',
			}),
			'part_song': forms.MultipleHiddenInput(attrs={
				'class': 'part_song',
			}),
			'part_vocal': forms.MultipleHiddenInput(attrs={
				'class': 'part_vocal',
			}),
			'explanation': forms.HiddenInput(attrs={
				'class': 'explanation',
			}),
		}

	def __init__(self, *args, **kwargs):
		super(PartEditFormforinline, self).__init__(*args, **kwargs)
		self.fields['part_name_short'].error_messages = {'required': 'パート番号を入力するか、削除してください'}

PartEditFormset = forms.inlineformset_factory(
	parent_model = Movie,
	model = Part,
	form = PartEditFormforinline,
	extra = 0,
	can_delete = True,
	can_order = True
)

class PartEditForm(forms.ModelForm):
	class Meta:
		model = Part
		fields = ('part_name', 'movie', 'participant', 'category', 'start_time', 'part_song', 'part_vocal', 'explanation')
		widgets = {
			'part_name': forms.TextInput(attrs={
				'class': 'part_name',
			}),
			'movie': forms.HiddenInput(attrs={
				'class': 'movie',
			}),
			'participant': forms.SelectMultiple(attrs={
				'class': 'participant',
			}),
			'category': forms.Select(attrs={
				'class': 'category',
			}),
			'start_time': forms.TextInput(attrs={
				'class': 'start_time',
			}),
			'part_song': forms.SelectMultiple(attrs={
				'class': 'part_song',
			}),
			'part_vocal': forms.SelectMultiple(attrs={
				'class': 'part_vocal',
			}),
			'explanation': forms.TextInput(attrs={
				'class': 'explanation',
			}),
		}

class StationInMovieEditForm(forms.ModelForm):
	BACKREL_CHOICES = [
		(0, '強制的につなげる'),
		(1, '通常接続'),
		(2, '強制的に離す'),
	]
	id_in_part = forms.IntegerField(
		label='順番', widget=forms.HiddenInput
	)
	back_rel = forms.ChoiceField(
		label='前駅関係', choices=BACKREL_CHOICES, widget=forms.Select
	)
	station_sung_name = forms.CharField(
		label='歌唱名', max_length=50
	)
	class Meta:
		model = StationInMovie
		fields = ('id_in_part', 'movie_part', 'station_service', 'station_sung_name', 'non_line', 'back_rel', 'is_sung')
		widgets = {
			'id_in_part': forms.TextInput(attrs={
				# 'class': 'id_in_part',
			}),
			'movie_part': forms.Select(attrs={
				# 'class': 'movie_part',
			}),
			'station_service': forms.HiddenInput(attrs={
				# 'class': 'station_service',
			}),
			'station_sung_name': forms.TextInput(attrs={
				# 'class': 'station_sung_name',
			}),
			'non_line': forms.CheckboxInput(attrs={
				# 'class': 'non_line',
			}),
			'back_rel': forms.TextInput(attrs={
				# 'class': 'back_rel',
			}),
			'is_sung': forms.CheckboxInput(attrs={
				# 'class': 'is_sung',
			}),
		}

StationInMovieEditFormset = forms.inlineformset_factory(
	parent_model = Part,
	model = StationInMovie,
	form = StationInMovieEditForm,
	extra = 0,
	can_delete = False
)


class CompanyRegisterForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('company_name', 'company_name_short', 'company_name_short_2', 'company_name_kana', 'company_color', 'area_code')

class LineRegisterForm(forms.ModelForm):
	class Meta:
		model = Line
		fields = ('category', 'line_name_formal', 'line_name', 'line_name_sub', 'company')

class StationRegisterForm(forms.ModelForm):
	class Meta:
		model = Station
		fields = ('category', 'station_code', 'station_group_code', 'station_name', 'station_name_kana', 'station_name_en', 'line', 'pref_code', 'e_status_old', 'sort_by_line')
		widgets = {
			'station_code': forms.TextInput(attrs={
				'class': 'station_code',
			}),
			'sort_by_line': forms.TextInput(attrs={
				'class': 'sort_by_line',
			}),
		}
StationRegisterFormset = forms.inlineformset_factory(
	parent_model = Line,
	fk_name = 'line',
	model = Station,
	form = StationRegisterForm,
	extra = 0,
	can_delete = False
)


class LineServiceRegisterForm(forms.ModelForm):
	class Meta:
		model = LineService
		fields = ('category', 'is_company_name', 'line_service_name', 'line_service_name_sub', 'company', 'is_formal', 'is_service', 'line_color')

class StationServiceRegisterForm(forms.ModelForm):
	class Meta:
		model = StationService
		fields = ('category', 'station', 'station_service_code', 'station_service_group_code', 'station_name', 'line_service', 'numbering_head', 'numbering_symbol', 'numbering_middle', 'numbering_number', 'sort_by_line_service', 'station_color')
		widgets = {
			'station': forms.HiddenInput(attrs={
				'class': 'station',
			}),
			'station_service_code': forms.TextInput(attrs={
				'class': 'station_service_code',
			}),
			'sort_by_line_service': forms.TextInput(attrs={
				'class': 'sort_by_line_service',
			}),
		}

StationServiceRegisterFormset = forms.inlineformset_factory(
	parent_model = LineService,
	fk_name = 'line_service',
	model = StationService,
	form = StationServiceRegisterForm,
	extra = 0,
	can_delete = False
)
