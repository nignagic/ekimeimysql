from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from . import serializer
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from .models import Prefecture, Railway_type, Company, Line, Station, LineService, StationService, Category, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie
from . import forms

import csv
from io import TextIOWrapper
# Create your views here.

class Top(generic.TemplateView):
	template_name = 'ekimeimysql1/top.html'

class MovieListView(generic.ListView):
	"""動画一覧"""
	template_name = 'ekimeimysql1/movielist.html'
	context_object_name = 'latest_movie_list'

	def get_queryset(self):
		return Movie.objects.all().order_by('channel').order_by('-published_at')

class StationServiceListbyLineView(generic.ListView):
	model = LineService
	template_name = 'ekimeimysql1/stationservicelistbylineview.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		lineservice = LineService.objects.get(line_service_code=self.kwargs['line_service_code'])
		stationservices = StationService.objects.filter(line_service_code=self.kwargs['line_service_code']).order_by('sort_by_line_service').exclude(station_code__e_status_old=2)
		transfers = {}
		stationserviceprev = 0
		for stationservice in stationservices:
			if stationserviceprev != stationservice.station_code.station_group_code:
				transfers[stationservice] = {}
				transferstations = Station.objects.filter(station_group_code=stationservice.station_code.station_group_code)
				for transferstation in transferstations:
					transfers[stationservice][transferstation] = StationService.objects.filter(station_code=transferstation.station_code).exclude(line_service_code=lineservice)
					if transfers[stationservice][transferstation].first() is None:
						del transfers[stationservice][transferstation]
			stationserviceprev = stationservice.station_code.station_group_code
		context = {
			'lineservice': lineservice,
			'transfers': transfers
		}
		return context

class LineServiceListbyCompanyView(generic.ListView):
	model = Company
	template_name = 'ekimeimysql1/company.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		companies = Company.objects.all()
		linebycompany = {}
		for company in companies:
			linebycompany[company] = LineService.objects.filter(company_code=company).order_by('sort_by_company')
			if linebycompany[company].first() is None:
				del linebycompany[company]
		context = {
			'linebycompany': linebycompany
		}
		return context

class StationServiceSearchView(generic.ListView):
	model = StationService
	template_name = 'ekimeimysql1/stationsearch.html'

	def get_context_data(self, **kwargs):
		q_word = self.request.GET.get('q')

		if q_word:
			stations = StationService.objects.filter(station_name__icontains=q_word).order_by('line_service_code').exclude(station_code__e_status_old=2)
		count = stations.count()
		context = {
			'word': q_word,
			'stations': stations,
			'count': count
		}
		return context

class MovieListbySongView(generic.ListView):
	model = Song
	template_name = 'ekimeimysql1/movielistbysong.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		parts = Part.objects.filter(song=self.kwargs['id'])
		movies = []
		for part in parts:
			movies.append(part.movie)
		movies_unique_order = sorted(set(movies), key=movies.index)

		song = Song.objects.get(pk=self.kwargs['id'])
		context = {
			'song': song,
			'movies': movies_unique_order
		}
		return context

class MovieListbyVocalView(generic.ListView):
	model = Vocal
	template_name = 'ekimei1/moviebyvocallist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		movies = Movie.objects.filter(vocal=self.kwargs['id']).order_by('-published_at')

		vocal = Vocal.objects.get(pk=self.kwargs['id'])
		context = {
			'vocal': vocal,
			'movies': movies
		}
		return context

def uploadPref(request):
	if 'csv' in request.FILES:
		prefectures = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			pref_cd = line[0]
			pref_name = line[1]
			pref = Prefecture(pref_code=pref_cd, pref_name=pref_name)
			prefectures.append(pref)
		Prefecture.objects.bulk_create(prefectures)

		return render(request, 'ekimeimysql1/upload.html')
	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadRailwayType(request):
	if 'csv' in request.FILES:
		railwaytypes = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			railway_type_code_2 = line[0]
			railway_type_code = line[1]
			railway_type_name = line[2]
			railwaytype = Railway_type(railway_type_code_2=railway_type_code_2, railway_type_code=railway_type_code, railway_type_name=railway_type_name)
			railwaytypes.append(railwaytype)
		Railway_type.objects.bulk_create(railwaytypes)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadCompany(request):
	if 'csv' in request.FILES:
		companies = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				railway_type_name = line[0]
				railway_type_code = line[1]
				company_code = line[2]
				company_name = line[3]
				company_name_short = line[4]
				company_name_short_2 = line[5]
				company_name_kana =line[6]
				company = Company(
					railway_type_name=railway_type_name,
					railway_type_code=railway_type_code,
					company_code=company_code,
					company_name=company_name,
					company_name_short=company_name_short,
					company_name_short_2=company_name_short_2,
					company_name_kana=company_name_kana)
				companies.append(company)
			else:
				i+=1
		Company.objects.bulk_create(companies)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadLine(request):
	if 'csv' in request.FILES:
		lines = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				railway_type_name = line[0]
				line_code = line[1]
				line_group_code = line[2]
				line_name_formal = line[3]
				line_name = line[4]
				line_name_sub = line[5]
				company_code = Company.objects.get(company_code=line[6])
				sort_by_company = line[7]
				start_station = line[8]
				end_station = line[9]
				business_type = line[10]
				is_freight = line[11]
				l = Line(
					railway_type_name=railway_type_name,
					line_code=line_code,
					line_group_code=line_group_code,
					line_name_formal=line_name_formal,
					line_name=line_name,
					line_name_sub=line_name_sub,
					company_code=company_code,
					sort_by_company=sort_by_company,
					start_station=start_station,
					end_station=end_station,
					business_type=business_type,
					is_freight=is_freight)
				lines.append(l)
			else:
				i+=1
		Line.objects.bulk_create(lines)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadStation(request):
	if 'csv' in request.FILES:
		stations = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				station_code = line[0]
				station_group_code = line[1]
				station_name = line[2]
				station_name_kana = line[3]
				station_name_en = line[4]
				railway_type = line[5]
				line_name = line[6]
				line_code = Line.objects.get(line_code=line[7])
				if line[8] != '':
					sort_by_line = line[8]
				else:
					sort_by_line = None;
				if line[9] != '':
					pref_code = Prefecture.objects.get(pref_code=line[9])
				else:
					pref_code = None;
				post_old = line[10]
				add_old = line[11]
				lon_old = line[12]
				lat_old = line[13]
				if line[14] != '':
					open_ymd_old = line[14]
				else:
					open_ymd_old = None;
				if line[15] != '':
					close_ymd_old = line[15]
				else:
					close_ymd_old = None;
				if line[16] != '':
					e_status_old = line[16]
				else:
					e_status_old = None;
				if line[17] != '':
					e_sort_old = line[17]
				else:
					e_sort_old = None;
				if line[18] != '':
					sort = line[18]
				else:
					sort = None;

				station = Station(
					station_code=station_code,
					station_group_code=station_group_code,
					station_name=station_name,
					station_name_kana=station_name_kana,
					station_name_en=station_name_en,
					railway_type=railway_type,
					line_name=line_name, 
					line_code=line_code,
					sort_by_line=sort_by_line,
					pref_code=pref_code,
					post_old=post_old,
					add_old=add_old,
					lon_old=lon_old,
					lat_old=lat_old,
					open_ymd_old=open_ymd_old,
					close_ymd_old=close_ymd_old,
					e_status_old=e_status_old,
					e_sort_old=e_sort_old,
					sort=sort)
				stations.append(station)
			else:
				i+=1
		Station.objects.bulk_create(stations)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadLineService(request):
	if 'csv' in request.FILES:
		lineservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				line_service_code = line[0]
				line_service_name_formal = line[1]
				line_service_name_formal_sub = line[2]

				company_name_simple = line[4]
				is_company_name = line[5]
				line_service_name = line[6]
				line_service_name_sub = line[7]
				company_code = Company.objects.get(company_code=line[8])
				sort_by_company = line[9]
				is_formal = line[10]
				is_service = line[11]
				lineservice = LineService(
					line_service_code=line_service_code,
					line_service_name_formal=line_service_name_formal,
					line_service_name_formal_sub=line_service_name_formal_sub,
					
					company_name_simple=company_name_simple,
					is_company_name=is_company_name,
					line_service_name=line_service_name,
					line_service_name_sub=line_service_name_sub,
					company_code=company_code,
					sort_by_company=sort_by_company,
					is_formal=is_formal,
					is_service=is_service)
				lineservices.append(lineservice)
			else:
				i+=1
		LineService.objects.bulk_create(lineservices)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadStationService(request):
	if 'csv' in request.FILES:
		stationservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				station_service_code = line[0]
				station_code = Station.objects.get(station_code=line[1])
				station_name = line[2]
				line_service_name = line[3]
				line_service_code = LineService.objects.get(line_service_code=line[4])
				numbering_symbol = line[5]
				numbering_number = line[6]
				sort_by_line_service = line[7]

				stationservice = StationService(
					station_service_code=station_service_code,
					station_code=station_code,
					station_name=station_name,
					line_service_name=line_service_name,
					line_service_code=line_service_code,
					numbering_symbol=numbering_symbol,
					numbering_number=numbering_number,
					sort_by_line_service=sort_by_line_service
					)
				stationservices.append(stationservice)
			else:
				i+=1
		StationService.objects.bulk_create(stationservices)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def StationDelete(request):
	Station.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def LineDelete(request):
	Line.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def CompanyDelete(request):
	Company.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def StationServiceDelete(request):
	StationService.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def LineServiceDelete(request):
	LineService.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def detail_movie(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	parts = Part.objects.filter(movie=movie).order_by('part_num')

	context = {
		'movie': movie,
		'parts': parts,
	}

	return render(request, 'ekimeimysql1/detail.html', context)

class MovieRegisterView(generic.CreateView):
	template_name = 'ekimeimysql1/register.html'
	model = Movie
	form_class = forms.MovieRegisterForm
	def get_success_url(self):
		return reverse_lazy('ekimeimysql1:part_edit', kwargs={'main_id': self.object.main_id})

def movie_part_edit(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	form = forms.MovieUpdateForm(request.POST or None, instance=movie)
	formset = forms.PartEditFormset(request.POST or None, instance=movie)
	if request.method == 'POST' and form.is_valid() and formset.is_valid():
		# parts = Part.objects.filter(movie=movie)
		# parts.delete()
		form.save()
		formset.save()
		queryset = Part.objects.filter(movie=main_id, part_num=1)
		if queryset.first() is None:
			return redirect('ekimeimysql1:detail', main_id=main_id)
		else:
			return redirect('ekimeimysql1:station_edit', main_id=main_id, part_num=1)

	context = {
		'movie': movie,
		'form': form,
		'formset': formset,
	}

	return render(request, 'ekimeimysql1/part_edit.html', context)

def movie_part_station_edit(request, main_id, part_num):
	part = get_object_or_404(Part, movie=main_id, part_num=part_num)
	formset = forms.StationInMovieEditFormset(request.POST or None, instance=part)
	if request.method == 'POST' and formset.is_valid():
		stations = StationInMovie.objects.filter(movie_part=part)
		stations.delete()
		formset.save()
		queryset = Part.objects.filter(movie=main_id, part_num=part_num+1)
		if queryset.first() is None:
			return redirect('ekimeimysql1:detail', main_id=main_id)
		else:
			return redirect('ekimeimysql1:station_edit', main_id=main_id, part_num=part_num+1)

	context = {
		'part': part,
		'formset': formset,
	}

	return render(request, 'ekimeimysql1/station_edit.html', context)

class SongCreate(generic.CreateView):
	"""楽曲データの作成"""
	model = Song
	fields = '__all__'
	success_url = reverse_lazy('ekimeimysql1:linelist')

class PopupSongCreate(SongCreate):
	"""ポップアップでの楽曲データ作成"""

	def form_valid(self, form):
		song = form.save()
		context = {
			'object_name': str(song),
			'object_pk': song.pk,
			'function_name': 'add_song'
		}
		return render(self.request, 'ekimeimysql1/close.html', context)

class ArtistCreate(generic.CreateView):
	"""歌手データの作成"""
	model = Artist
	fields = '__all__'
	success_url = reverse_lazy('ekimeimysql1:linelist')

class PopupArtistCreate(ArtistCreate):
	"""ポップアップでの歌手データ作成"""

	def form_valid(self, form):
		artist = form.save()
		context = {
			'object_name': str(artist),
			'object_pk': artist.pk,
			'function_name': 'add_artist'
		}
		return render(self.request, 'ekimeimysql1/close.html', context)

class VocalCreate(generic.CreateView):
	"""ボーカルデータの作成"""
	model = Vocal
	fields = '__all__'
	success_url = reverse_lazy('ekimeimysql1:linelist')

class PopupVocalCreate(VocalCreate):
	"""ポップアップでのボーカルデータ作成"""

	def form_valid(self, form):
		vocal = form.save()
		context = {
			'object_name': str(vocal),
			'object_pk': vocal.pk,
			'function_name': 'add_vocal'
		}
		return render(self.request, 'ekimeimysql1/close.html', context)

def lineprefset(request):
	stations = Station.objects.all()
	for station in stations:
		line = station.line_code
		pref = station.pref_code
		line.pref_codes.add(pref)

	return render(request, 'ekimeimysql1/lineprefset.html')

def lineServiceprefset(request):
	stationservices = StationService.objects.all()
	for stationservice in stationservices:
		line = stationservice.line_service_code
		pref = stationservice.station_code.pref_code
		line.pref_codes.add(pref)

	return render(request, 'ekimeimysql1/lineprefset.html')

class StationServiceViewSet(generics.ListAPIView):
	serializer_class = serializer.StationServiceSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['line_cd']
		return StationService.objects.filter(line_service_code=query_my_name)

class LineServiceViewSet(generics.ListAPIView):
	serializer_class = serializer.LineServiceSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['pref_code']
		return LineService.objects.filter(pref_codes__pref_code=query_my_name)

class StationServiceSearchViewSet(generics.ListAPIView):
	serializer_class = serializer.StationSearchSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['words']
		return StationService.objects.filter(station_name__contains=query_my_name)

# class TransferViewSet(generics.ListAPIView):
# 	serializer_class = serializer.LineSerializer
# 	def get_queryset(self):
# 		station = StationService.objects.get(station_code=self.kwargs['station_service_code'])
# 		stations = StationService.objects.filter(station_group_code=station.station_g_cd)
# 		lines = []
# 		for station in stations:
# 			lines.append(station.line_cd)
# 		return lines

class PartStationViewSet(generics.ListAPIView):
	serializer_class = serializer.StationInMovieSerializer
	def get_queryset(self):
		stations = StationInMovie.objects.filter(movie_part=self.kwargs['id'])
		return stations

class NameViewSet(generics.ListAPIView):
	serializer_class = serializer.NameSerializer
	def get_queryset(self):
		names = Name.objects.all()
		return names

class SongViewSet(generics.ListAPIView):
	serializer_class = serializer.SongSerializer
	def get_queryset(self):
		songs = Song.objects.all()
		return songs

class VocalViewSet(generics.ListAPIView):
	serializer_class = serializer.VocalSerializer
	def get_queryset(self):
		vocals = Vocal.objects.all()
		return vocals