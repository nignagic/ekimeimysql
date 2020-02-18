from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import Movie, Part, StationInMovie

class MovieRegisterForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_comment', 'description', 'reg_date', 'song', 'vocal', 'is_collab', 'parent', 'explanation')
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
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_dislike', 'n_comment', 'description', 'reg_date', 'song', 'vocal', 'is_collab')
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

class PartEditForm(forms.ModelForm):
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

PartEditFormset = forms.inlineformset_factory(
	parent_model = Movie,
	model = Part,
	form = PartEditForm,
	extra = 1,
	can_delete = True,
	can_order = True
)

class StationInMovieEditForm(forms.ModelForm):
	BACKREL_CHOICES = [
		(0, '同一駅'),
		(1, 'つながっている'),
		(2, '離れている'),
	]
	id_in_movie = forms.IntegerField(
		label='順番', widget=forms.HiddenInput
	)
	back_rel = forms.ChoiceField(
		label='前駅関係', choices=BACKREL_CHOICES, widget=forms.Select
	)
	station_service_name = forms.CharField(
		label='歌唱名', max_length=50
	)
	class Meta:
		model = StationInMovie
		fields = ('id_in_movie', 'movie_part', 'station_service_code', 'station_service_name', 'non_line', 'back_rel')
		widgets = {
			'id_in_movie': forms.TextInput(attrs={
				'class': 'id_in_movie',
			}),
			'movie_part': forms.Select(attrs={
				'class': 'movie_part',
			}),
			'station_service_code': forms.HiddenInput(attrs={
				'class': 'station_service_code',
			}),
			'station_service_name': forms.TextInput(attrs={
				'class': 'station_service_name',
			}),
			'non_line': forms.CheckboxInput(attrs={
				'class': 'non_line',
			}),
			'back_rel': forms.TextInput(attrs={
				'class': 'back_rel',
			}),
		}

StationInMovieEditFormset = forms.inlineformset_factory(
	parent_model = Part,
	model = StationInMovie,
	form = StationInMovieEditForm,
	extra = 0,
	can_delete = False
)