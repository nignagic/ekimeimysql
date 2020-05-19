from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from . import serializer
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
	LoginView, LogoutView
)
from .forms import LoginForm

from .models import Railway_type, Country, Region, Prefecture, Company, BelongsCategory, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie, get_next_station, get_next_stationservice, LineInMovie
from . import forms

import csv
from io import TextIOWrapper

from datetime import date
import urllib
from django.http import HttpResponse
from itertools import groupby

# Create your views here.

class Top(generic.ListView):
	model = Movie
	template_name = 'ekimeimysql1/top.html'

	def get_context_data(self):
		movies = Movie.objects.all().order_by('-published_at')[:6]
		context = {
			'movies': movies
		}
		return context

class Login(LoginView):
	"""ログインページ"""
	form_class = LoginForm
	template_name = 'ekimeimysql1/login.html'

class Logout(LogoutView):
	"""ログアウトページ"""
	template_name = 'ekimeimysql1/top.html'


class StationListbyLineView(generic.ListView):
	model = Line
	template_name = 'ekimeimysql1/stationlistbyline.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		line = Line.objects.get(pk=self.kwargs['line_pk'])
		stations = Station.objects.filter(line=self.kwargs['line_pk'])
		transfers = {}
		for station in stations:
			transfers[station] = Station.objects.filter(station_group_code=station.station_group_code).exclude(line=line)
		context = {
			'line': line,
			'transfers': transfers
		}
		return context

class StationServiceListbyLineView(generic.ListView):
	model = LineService
	template_name = 'ekimeimysql1/stationservicelistbyline.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
		stationservices = StationService.objects.filter(line_service=self.kwargs['line_service_pk']).filter(station__e_status_old=0).order_by('sort_by_line_service')
		transfers = {}
		stationserviceprev = 0
		for stationservice in stationservices:
			if stationserviceprev != stationservice.station.station_group_code:
				transfers[stationservice] = {}
				transferstations = Station.objects.filter(station_group_code=stationservice.station.station_group_code)
				for transferstation in transferstations:
					transfers[stationservice][transferstation] = StationService.objects.filter(station=transferstation.pk).exclude(line_service=lineservice)
					if transfers[stationservice][transferstation].first() is None:
						del transfers[stationservice][transferstation]
			stationserviceprev = stationservice.station.station_group_code
		context = {
			'lineservice': lineservice,
			'transfers': transfers
		}
		return context

class SongTopView(generic.ListView):
	model = Region
	template_name = 'ekimeimysql1/songtop.html'

class RailwayTopView(generic.ListView):
	model = Region
	template_name = 'ekimeimysql1/railwaytop.html'

	def get_context_data(self, **kwargs):
		countries = Country.objects.all()
		regions = {}
		for country in countries:
			regions[country] = Region.objects.filter(country=country)

		belongscategory = BelongsCategory.objects.all().exclude(pk=0)

		context = {
			'belongscategory': belongscategory,
			'regions': regions,
		}

		return context

class LineServiceListbyCategoryView(generic.ListView):
	model = LineService
	template_name = 'ekimeimysql1/lineservicelistbycategory.html'

	def get_context_data(self, **kwargs):
		category = BelongsCategory.objects.get(pk=self.kwargs['pk'])
		lineservices = LineService.objects.filter(category=category)

		context = {
			'category': category,
			'lineservices': lineservices
		}

		return context

class CompanyListbyRegionView(generic.ListView):
	model = Company
	template_name = 'ekimeimysql1/companylistbyregion.html'

	def get_context_data(self, **kwargs):
		region = Region.objects.get(pk=self.kwargs['pk'])
		prefs = Prefecture.objects.filter(region=region)
		companies = Company.objects.none()
		for pref in prefs:
			lineservices = LineService.objects.filter(pref_codes=pref)
			for lineservice in lineservices:
				companies |= Company.objects.filter(pk=lineservice.company.pk)

		context = {
			'region': region,
			'prefs': prefs,
			'companies': companies
		}

		return context

class LineServiceListbyCompanyView(generic.ListView):
	model = Company
	template_name = 'ekimeimysql1/lineservicelistbycompany.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		company = Company.objects.get(pk=self.kwargs['pk'])
		lineservices = LineService.objects.filter(company=company).order_by('sort_by_company')
		
		context = {
			'company': company,
			'lineservices': lineservices
		}
		return context

class LineServiceListbyPrefectureView(generic.ListView):
	model = LineService
	template_name = 'ekimeimysql1/lineservicelistbyprefecture.html'

	def get_context_data(self, **kwargs):
		pref = Prefecture.objects.get(pk=self.kwargs['pk'])
		lineservices = LineService.objects.filter(pref_codes=pref)

		context = {
			'pref': pref,
			'lineservices': lineservices
		}

		return context

# class StationSearchView(generic.ListView):
# 	model = StationService
# 	template_name = 'ekimeimysql1/stationsearch.html'

# 	def get_context_data(self, **kwargs):
# 		q_word = self.request.GET.get('q')

# 		if q_word:
# 			stations = StationService.objects.filter(station_name__icontains=q_word).filter(station__e_status_old=0).order_by('line_service')
# 		count = stations.count()
# 		context = {
# 			'word': q_word,
# 			'stations': stations,
# 			'count': count
# 		}
# 		return context

class NoticeView(generic.TemplateView):
	template_name = 'ekimeimysql1/notice.html'


class MovieListView(generic.ListView):
	"""動画一覧"""
	model = Movie
	template_name = 'ekimeimysql1/newarrival.html'
	queryset = Movie.objects.all()
	paginate_by = 12
	ordering = '-published_at'


class StationServiceListbyLineView(generic.ListView):
	model = LineService
	template_name = 'ekimeimysql1/stationservicelistbylineview.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
		stationservices = StationService.objects.filter(line_service=self.kwargs['line_service_pk']).order_by('sort_by_line_service').exclude(station__e_status_old=2)
		transfers = {}
		stationserviceprev = 0
		for stationservice in stationservices:
			if stationserviceprev != stationservice.station.station_group_code:
				transfers[stationservice] = {}
				transferstations = Station.objects.filter(station_group_code=stationservice.station.station_group_code)
				for transferstation in transferstations:
					transfers[stationservice][transferstation] = StationService.objects.filter(station=transferstation.pk).exclude(line_service=lineservice)
					if transfers[stationservice][transferstation].first() is None:
						del transfers[stationservice][transferstation]
			stationserviceprev = stationservice.station.station_group_code
		context = {
			'lineservice': lineservice,
			'transfers': transfers
		}
		return context

# class LineServiceListbyCompanyView(generic.ListView):
# 	model = Company
# 	template_name = 'ekimeimysql1/company.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)

# 		companies = Company.objects.all()
# 		linebycompany = {}
# 		for company in companies:
# 			linebycompany[company] = LineService.objects.filter(company=company).order_by('sort_by_company')
# 			if linebycompany[company].first() is None:
# 				del linebycompany[company]
# 		context = {
# 			'linebycompany': linebycompany
# 		}
# 		return context

class StationServiceSearchView(generic.ListView):
	model = StationService
	template_name = 'ekimeimysql1/stationsearch.html'

	def get_context_data(self, **kwargs):
		q_word = self.request.GET.get('q')

		if q_word:
			stationservices = StationService.objects.filter(station_name__icontains=q_word).order_by('line_service')
		count = stationservices.count()
		context = {
			'word': q_word,
			'stationservices': stationservices,
			'count': count
		}
		return context

class MovieListbyLineView(generic.ListView):
	model = Line
	template_name = 'ekimeimysql1/movielistbyline.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = Movie.objects.none()
		line = Line.objects.get(pk=self.kwargs['line_pk'])
		stations = Station.objects.filter(line=self.kwargs['line_pk']).order_by('sort_by_line')
		for station in stations:
			stationservices = StationService.objects.filter(station=station.pk)
			for stationservice in stationservices:
				stationinmovies = StationInMovie.objects.filter(station_service=stationservice)
				for movie in stationinmovies:
					queryset |= Movie.objects.filter(pk=movie.movie_part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		line = Line.objects.get(pk=self.kwargs['line_pk'])
		stations = Station.objects.filter(line=self.kwargs['line_pk']).order_by('sort_by_line')
		lineservices = LineService.objects.none()
		for station in stations:
			stationservices = StationService.objects.filter(station=station.pk)
			for stationservice in stationservices:
				lineservices |= LineService.objects.filter(pk=stationservice.line_service.pk)

		context['line'] = line
		context['stations'] = stations
		context['lineservices'] = lineservices
		
		return context

class MovieListbyStationView(generic.ListView):
	model = Station
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbystation.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = Movie.objects.none()
		station = Station.objects.get(pk=self.kwargs['station_pk'])
		stationservices = StationService.objects.filter(station=station)
		for stationservice in stationservices:
			stationinmovies = StationInMovie.objects.filter(station_service=stationservice)
			for stationinmovie in stationinmovies:
				queryset |= Movie.objects.filter(pk=stationinmovie.movie_part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		station = Station.objects.get(pk=self.kwargs['station_pk'])
		stationservices = StationService.objects.filter(station=station)
		transfers = Station.objects.filter(station_group_code=station.station_group_code)

		context['station'] = station
		context['stationservices'] = stationservices
		context['transfers'] = transfers
		
		return context

# class MovieListbyLineServiceView(generic.ListView):
# 	model = LineService
# 	paginate_by = 10
# 	template_name = 'ekimeimysql1/movielistbylineservice.html'

# 	def get_queryset(self):
# 		queryset = super().get_queryset()
# 		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
# 		stationservices = StationService.objects.filter(line_service=self.kwargs['line_service_pk']).order_by('sort_by_line_service')
# 		queryset = Movie.objects.none()
# 		for stationservice in stationservices:
# 			stationinmovies = StationInMovie.objects.filter(station_service=stationservice)
# 			for movie in stationinmovies:
# 				queryset |= Movie.objects.filter(pk=movie.movie_part.movie.pk)
# 		return queryset

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)

# 		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
# 		stationservices = StationService.objects.filter(line_service=self.kwargs['line_service_pk']).order_by('sort_by_line_service')
# 		lines = Line.objects.none()
# 		for stationservice in stationservices:
# 			lines |= Line.objects.filter(pk=stationservice.station.line.pk)

# 		context['lineservice'] = lineservice
# 		context['stationservices'] = stationservices
# 		context['lines'] = lines
		
# 		return context

class MovieListbyLineServiceView(generic.ListView):
	model = Movie
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbylineservice.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = Movie.objects.none()
		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
		lineinmovies = LineInMovie.objects.filter(line_service=lineservice)
		for lineinmovie in lineinmovies:
			queryset |= Movie.objects.filter(pk=lineinmovie.movie_part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		lineservice = LineService.objects.get(pk=self.kwargs['line_service_pk'])
		stationservices = StationService.objects.filter(line_service=self.kwargs['line_service_pk']).order_by('sort_by_line_service')
		lines = lineservice.line.all()

		context['lineservice'] = lineservice
		context['stationservices'] = stationservices
		context['lines'] = lines
		
		return context


class MovieListbyStationServiceView(generic.ListView):
	model = Movie
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbystationservice.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		stationservice = StationService.objects.get(pk=self.kwargs['station_service_pk'])
		stationinmovies = StationInMovie.objects.filter(station_service=stationservice)
		queryset = Movie.objects.none()
		for stationinmovie in stationinmovies:
			queryset |= Movie.objects.filter(pk=stationinmovie.movie_part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		stationservice = StationService.objects.get(pk=self.kwargs['station_service_pk'])
		stations = Station.objects.filter(station_group_code=stationservice.station.station_group_code)
		transfers = {}
		for station in stations:
			transfers[station] = StationService.objects.filter(station=station.pk)

		different_line = False
		stationservicegroup = StationService.objects.filter(station_service_group_code=stationservice.station_service_group_code).exclude(pk=stationservice.pk)
		if stationservicegroup:
			if stationservicegroup[0].station.line != stationservice.station.line:
				different_line = True
			else:
				for group in stationservicegroup:
					stationinmovies = StationInMovie.objects.filter(station_service=group)
					for stationinmovie in stationinmovies:
						movies |= Movie.objects.filter(pk=stationinmovie.movie_part.movie.pk)

		context['stationservice'] = stationservice
		context['transfers'] = transfers
		context['stationservicegroup'] = stationservicegroup
		context['different_line'] = different_line
		
		return context

class MovieListbyArtistView(generic.ListView):
	model = Artist
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbyartist.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		artist = Artist.objects.get(pk=self.kwargs['id'])
		songs = Song.objects.filter(artist=artist)
		queryset = Movie.objects.none()
		for song in songs:
			queryset |= Movie.objects.filter(song=song)
			parts = Part.objects.filter(part_song=song)
			for part in parts:
				queryset |= Movie.objects.filter(pk=part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		artist = Artist.objects.get(pk=self.kwargs['id'])
		songs = Song.objects.filter(artist=artist)

		context['artist'] = artist
		context['songs'] = songs

		return context

class MovieListbySongView(generic.ListView):
	model = Movie
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbysong.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		parts = Part.objects.filter(part_song=self.kwargs['id'])
		queryset = Movie.objects.none()
		for part in parts:
			queryset |= Movie.objects.filter(pk=part.movie.pk)
		queryset |= Movie.objects.filter(song=self.kwargs['id'])
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		song = Song.objects.get(pk=self.kwargs['id'])
		context['song'] = song

		return context

class MovieListbyVocalView(generic.ListView):
	model = Movie
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbyvocal.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		parts = Part.objects.filter(part_vocal=self.kwargs['id'])
		queryset = Movie.objects.none()
		for part in parts:
			queryset |= Movie.objects.filter(pk=part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		vocal = Vocal.objects.get(pk=self.kwargs['id'])
		context['vocal'] = vocal
		return context

class MovieListbyChannelView(generic.ListView):
	model = YoutubeChannel
	paginate_by = 10
	template_name = 'ekimeimysql1/movielistbychannel.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = Movie.objects.filter(channel=self.kwargs['channel_id'])
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		channel = YoutubeChannel.objects.get(pk=self.kwargs['channel_id'])
		context['channel'] = channel

		return context

class ArtistListView(generic.ListView):
	model = Artist
	template_name = 'ekimeimysql1/artistlist.html'

class SongListView(generic.ListView):
	model = Song
	template_name = 'ekimeimysql1/songlist.html'

class VocalListView(generic.ListView):
	model = Vocal
	template_name = 'ekimeimysql1/vocallist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		vocals = Vocal.objects.all()

		context = {
			'vocals': vocals
		}
		return context

class CreatorTopView(generic.ListView):
	model = Creator
	template_name = 'ekimeimysql1/creatortop.html'

class EachCreatorView(generic.ListView):
	model = Movie
	template_name = 'ekimeimysql1/eachcreator.html'
	paginate_by = 100

	def get_queryset(self):
		queryset = super().get_queryset()
		names = Name.objects.filter(creator=self.kwargs['id'])
		queryset = Movie.objects.none()
		for name in names:
			parts = Part.objects.filter(participant=name)
			for part in parts:
				queryset |= Movie.objects.filter(pk=part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		creator = Creator.objects.get(pk=self.kwargs['id'])
		names = Name.objects.filter(creator=creator.pk)
		channels = YoutubeChannel.objects.filter(creator=creator.pk)
		context['creator'] = creator
		context['names'] = names
		context['channels'] = channels
		return context

class MovieListbyNameView(generic.ListView):
	model = Movie
	template_name = 'ekimeimysql1/movielistbyname.html'
	paginate_by = 100

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = Movie.objects.none()
		name = Name.objects.get(pk=self.kwargs['id'])
		parts = Part.objects.filter(participant=name)
		for part in parts:
			queryset |= Movie.objects.filter(pk=part.movie.pk)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		name = Name.objects.get(pk=self.kwargs['id'])
		creator = Creator.objects.get(pk=name.creator.pk)
		context['name'] = name
		context['creator'] = creator
		return context

class ChannelListView(generic.ListView):
	model = YoutubeChannel
	template_name = 'ekimeimysql1/channellist.html'

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

def uploadCountry(request):
	if 'csv' in request.FILES:
		countries = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			country_code = line[0]
			country_name = line[1]
			country = Country(
				country_code=country_code,
				country_name=country_name
			)
			countries.append(country)
		Country.objects.bulk_create(countries)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadRegion(request):
	if 'csv' in request.FILES:
		regions = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			region_code = line[0]
			region_name = line[1]
			country = Country.objects.get(country_code=line[2])
			region = Region(
				region_code=region_code,
				region_name=region_name,
				country=country
			)
			regions.append(region)
		Region.objects.bulk_create(regions)

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadPrefecture(request):
	if 'csv' in request.FILES:
		prefectures = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			pref_code = line[0]
			pref_name = line[1]
			region = Region.objects.get(region_code=line[2])
			prefecture = Prefecture(
				pref_code=pref_code,
				pref_name=pref_name,
				region=region
			)
			prefectures.append(prefecture)
		Prefecture.objects.bulk_create(prefectures)

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
				company_name_kana = line[6]
				company_color = line[7]
				area_code = line[8]
				sort_by_area = line[9]
				company = Company(
					railway_type_name=railway_type_name,
					railway_type_code=railway_type_code,
					company_code=company_code,
					company_name=company_name,
					company_name_short=company_name_short,
					company_name_short_2=company_name_short_2,
					company_name_kana=company_name_kana,
					company_color=company_color,
					area_code=area_code,
					sort_by_area=sort_by_area)
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
		updatelines = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				if line[12] == 'create':
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
				elif line[12] == 'update':
					l = Line.objects.get(line_code=line[1])
					l.railway_type_name = line[0]
					# l.line_code = line[1]
					l.line_group_code = line[2]
					l.line_name_formal = line[3]
					l.line_name = line[4]
					l.line_name_sub = line[5]
					l.company_code = Company.objects.get(company_code=line[6])
					l.sort_by_company = line[7]
					l.start_station = line[8]
					l.end_station = line[9]
					l.business_type = line[10]
					l.is_freight = line[11]
					updatelines.append(l)
			else:
				i+=1
		Line.objects.bulk_create(lines)
		Line.objects.bulk_update(updatelines, fields=['railway_type_name', 'line_code', 'line_group_code', 'line_name_formal', 'line_name', 'line_name_sub', 'company_code', 'sort_by_company', 'start_station', 'end_station', 'business_type', 'is_freight'])

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')
def uploadStation(request):
	if 'csv' in request.FILES:
		stations = []
		updatestations = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				if line[24] == 'create':
					station_code = line[2]
					station_group_code = line[3]
					station_name = line[6]
					station_name_kana = line[7]
					station_name_en = line[8]
					railway_type = line[9]
					line_name = line[10]
					line_code = Line.objects.get(line_code=line[11])
					if line[12] != '':
						sort_by_line = line[12]
					else:
						sort_by_line = None;
					pref_code = Prefecture.objects.get(pref_code=line[14])
					if line[14] != '':
						pref_cd_old = line[14]
					else:
						pref_cd_old = None;
					post_old = line[15]
					add_old = line[16]
					lon_old = line[17]
					lat_old = line[18]
					if line[19] != '':
						open_ymd_old = line[19]
					else:
						open_ymd_old = None;
					if line[20] != '':
						close_ymd_old = line[20]
					else:
						close_ymd_old = None;
					if line[21] != '':
						e_status_old = line[21]
					else:
						e_status_old = None;
					if line[22] != '':
						e_sort_old = line[22]
					else:
						e_sort_old = None;
					if line[23] != '':
						sort = line[23]
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
						pref_code=pref_code,
						sort_by_line=sort_by_line,
						pref_cd_old=pref_cd_old,
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
				elif line[24] == 'update':
					station = Station.objects.get(station_code=line[2])
					# station_code = line[2]
					station.station_group_code = line[3]
					station.station_name = line[6]
					station.station_name_kana = line[7]
					station.station_name_en = line[8]
					station.railway_type = line[9]
					station.line_name = line[10]
					station.line_code = Line.objects.get(line_code=line[11])
					if line[12] != '':
						station.sort_by_line = line[12]
					else:
						station.sort_by_line = None;
					station.pref_code = Prefecture.objects.get(pref_code=line[14])
					if line[14] != '':
						station.pref_cd_old = line[14]
					else:
						station.pref_cd_old = None;
					station.post_old = line[15]
					station.add_old = line[16]
					station.lon_old = line[17]
					station.lat_old = line[18]
					if line[19] != '':
						station.open_ymd_old = line[19]
					else:
						station.open_ymd_old = None;
					if line[20] != '':
						station.close_ymd_old = line[20]
					else:
						station.close_ymd_old = None;
					if line[21] != '':
						station.e_status_old = line[21]
					else:
						station.e_status_old = None;
					if line[22] != '':
						station.e_sort_old = line[22]
					else:
						station.e_sort_old = None;
					if line[23] != '':
						station.sort = line[23]
					else:
						station.sort = None;
					updatestations.append(station)				
			else:
				i+=1
		Station.objects.bulk_create(stations)
		Station.objects.bulk_update(updatestations, fields=[
			'station_code',
			'station_group_code',
			'station_name',
			'station_name_kana',
			'station_name_en',
			'railway_type',
			'line_name',
			'line_code',
			'pref_code',
			'sort_by_line',
			'pref_cd_old',
			'post_old',
			'add_old',
			'lon_old',
			'lat_old',
			'open_ymd_old',
			'close_ymd_old',
			'e_status_old',
			'e_sort_old'
		])

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadLineService(request):
	if 'csv' in request.FILES:
		lineservices = []
		updatelineservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				if line[19] == 'create':
					line_service_code = line[4]
					line_service_name_formal = line[5]
					line_service_name_formal_sub = line[6]

					company_name_simple = line[7]
					is_company_name = line[8]
					line_service_name = line[9]
					line_service_name_sub = line[10]
					company_code = Company.objects.get(company_code=line[14])
					sort_by_company = line[15]
					line_color = line[16]
					is_formal = line[17]
					is_service = line[18]
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
						is_service=is_service,
						line_color=line_color)
					lineservices.append(lineservice)
				elif line[19] == 'update':
					lineservice = LineService.objects.get(line_service_code=line[4])
					lineservice.line_service_name_formal = line[5]
					lineservice.line_service_name_formal_sub = line[6]

					lineservice.company_name_simple = line[7]
					lineservice.is_company_name = line[8]
					lineservice.line_service_name = line[9]
					lineservice.line_service_name_sub = line[10]
					lineservice.company_code = Company.objects.get(company_code=line[14])
					lineservice.sort_by_company = line[15]
					lineservice.line_color = line[16]
					lineservice.is_formal = line[17]
					lineservice.is_service = line[18]
					updatelineservices.append(lineservice)
			else:
				i+=1
		LineService.objects.bulk_create(lineservices)
		LineService.objects.bulk_update(updatelineservices, fields=[
			'line_service_code',
			'line_service_name_formal',
			'line_service_name_formal_sub',
			'company_name_simple',
			'is_company_name',
			'line_service_name',
			'line_service_name_sub',
			'company_code',
			'sort_by_company',
			'is_formal',
			'is_service',
			'line_color'
		])

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def uploadStationService(request):
	if 'csv' in request.FILES:
		stationservices = []
		updatestationservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				if line[19] == 'create':
					station_service_code = line[3]
					station_code = Station.objects.get(station_code=line[4])
					station_name = line[5]
					line_service_name = line[10]
					line_service_code = LineService.objects.get(line_service_code=line[11])
					numbering_head = line[12]
					numbering_symbol = line[13]
					numbering_middle = line[14]
					numbering_number = line[15]
					sort_by_line_service = line[16]
					station_color = line[17]

					stationservice = StationService(
						station_service_code=station_service_code,
						station_code=station_code,
						station_name=station_name,
						line_service_name=line_service_name,
						line_service_code=line_service_code,
						numbering_head=numbering_head,
						numbering_symbol=numbering_symbol,
						numbering_middle=numbering_middle,
						numbering_number=numbering_number,
						sort_by_line_service=sort_by_line_service,
						station_color=station_color
						)
					stationservices.append(stationservice)
				elif line[19] == 'update':
					stationservice = StationService.objects.get(station_service_code=line[3])
					stationservice.station_code = Station.objects.get(station_code=line[4])
					stationservice.station_name = line[5]
					stationservice.line_service_name = line[10]
					stationservice.line_service_code = LineService.objects.get(line_service_code=line[11])
					stationservice.numbering_head = line[12]
					stationservice.numbering_symbol = line[13]
					stationservice.numbering_middle = line[14]
					stationservice.numbering_number = line[15]
					stationservice.sort_by_line_service = line[16]
					stationservice.station_color = line[17]
					updatestationservices.append(stationservice)
			else:
				i+=1
		StationService.objects.bulk_create(stationservices)
		StationService.objects.bulk_update(updatestationservices, fields=[
			'station_service_code',
			'station_code',
			'station_name',
			'line_service_name',
			'line_service_code',
			'numbering_head',
			'numbering_symbol',
			'numbering_middle',
			'numbering_number',
			'sort_by_line_service',
			'station_color'
		])

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')

def CompanyDelete(request):
	Company.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def LineDelete(request):
	Line.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def StationDelete(request):
	Station.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def LineServiceDelete(request):
	LineService.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def StationServiceDelete(request):
	StationService.objects.all().delete()
	return render(request, 'ekimeimysql1/upload.html')

def StationServiceExport(request):
	t = date.today()
	output_name = t.strftime('%Y%m') + '_stationservice.csv'
	file_name = urllib.parse.quote((u'CSVファイル.csv').encode("utf8"))

	response = HttpResponse(content_type='text/csv; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(file_name)
	writer = csv.writer(response)

	header = ['種類ID', '種類名' , '駅コード(運行系統)', '駅コード(正式)[code]', '駅名(正式)[code]', '駅コード(正式)[id]', '駅名(正式)[id]', '駅名', '駅グループコード(運行系統)', '路線名(運行系統)', '路線コード(運行系統)[code]', '路線名(運行系統)[code]', '路線コード(運行系統)[id]', '路線名(運行系統)[id]', 'ナンバリング接頭辞', '路線記号', 'ナンバリングハイフン', '駅番号', '路線(運行系統)ごとの並び順', '駅カラー']
	writer.writerow(header)

	stationservices = StationService.objects.all()
	for stationservice in stationservices:
		category = ""
		category_name = ""
		station_service_code = stationservice.station_service_code
		station_code = stationservice.station_code.station_code
		station_code_name = stationservice.station_code.station_name
		station = stationservice.station.id
		station_id_name = stationservice.station.station_name
		station_name = stationservice.station_name
		station_service_group_code = stationservice.station_service_group_code
		line_service_name = stationservice.line_service_name
		line_service_code = stationservice.line_service_code.line_service_code
		line_service_code_name = stationservice.line_service_code.line_service_name
		line_service = stationservice.line_service.id
		line_service_id_name = stationservice.line_service.line_service_name
		numbering_head = stationservice.numbering_head
		numbering_symbol = stationservice.numbering_symbol
		numbering_middle = stationservice.numbering_middle
		numbering_number = stationservice.numbering_number
		sort_by_line_service = stationservice.sort_by_line_service
		station_color = stationservice.station_color

		row = []
		row += [category, category_name, station_service_code, station_code, station_code_name, station, station_id_name, station_name, station_service_group_code, line_service_name, line_service_code, line_service_code_name, line_service, line_service_id_name, numbering_head, numbering_symbol, numbering_middle, numbering_number, sort_by_line_service, station_color]

		writer.writerow(row)

	return response


def EmergencyCode(request):
	parts = Part.objects.all()
	lineinmovies = []
	for part in parts:
		stations = StationInMovie.objects.filter(movie_part=part)
		lines = LineService.objects.none()
		for station in stations:
			lines |= LineService.objects.filter(pk=station.station_service.line_service.pk)
		for line in lines:
			lineinmovie = LineInMovie(movie_part=part, line_service=line)
			lineinmovies.append(lineinmovie)
	LineInMovie.objects.bulk_create(lineinmovies)

	return a




class CompanyRegisterView(generic.CreateView):
	template_name = 'ekimeimysql1/companyregister.html'
	model = Company
	form_class = forms.CompanyRegisterForm
	def get_success_url(self):
		return reverse_lazy('ekimeimysql1:lineregister', kwargs={'company_pk': self.object.pk})

def LineRegisterView(request, company_pk):
	company = get_object_or_404(Company, pk=company_pk)
	form = forms.LineRegisterForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		line = Line.objects.latest('pk')
		lineservice, created = LineService.objects.get_or_create(category=line.category, line_service_name=line.line_name, company=line.company, is_formal=1)
		return redirect('ekimeimysql1:stationregister', line_pk=line.pk)

	context = {
		'company': company,
		'form': form
	}

	return render(request, 'ekimeimysql1/lineregister.html', context)

def StationRegisterView(request, line_pk):
	line = get_object_or_404(Line, pk=line_pk)
	last_code = get_next_station()
	formset = forms.StationRegisterFormset(request.POST or None, instance=line)
	if request.method == 'POST' and formset.is_valid():
		formset.save()
		stations = Station.objects.filter(line=line)
		prefs = Prefecture.objects.none()
		for station in stations:
			prefs |= Prefecture.objects.filter(pk=station.pref_code.pk)
		for pref in prefs:
			line.pref_codes.add(pref)
		return redirect('ekimeimysql1:railwaysearch')

	context = {
		'line': line,
		'last_code': last_code,
		'formset': formset
	}

	return render(request, 'ekimeimysql1/stationregister.html', context)

def LineServiceRegisterView(request, company_pk):
	company = get_object_or_404(Company, pk=company_pk)
	form = forms.LineServiceRegisterForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('ekimeimysql1:stationserviceregister', line_service_pk=pk)

	context = {
		'company': company,
		'form': form
	}

	return render(request, 'ekimeimysql1/lineserviceregister.html', context)

def StationServiceRegisterView(request, line_service_pk):
	lineservice = get_object_or_404(LineService, pk=line_service_pk)
	lines = Line.objects.filter(company=lineservice.company)
	last_code = get_next_stationservice()
	formset = forms.StationServiceRegisterFormset(request.POST or None, instance=lineservice)
	if request.method == 'POST' and formset.is_valid():
		formset.save()
		stationservices = StationService.objects.filter(line_service=lineservice)
		prefs = Prefecture.objects.none()
		lines = Line.objects.none()
		for stationservice in stationservices:
			prefs |= Prefecture.objects.filter(pk=stationservice.station.pref_code.pk)
			lines |= Line.objects.filter(pk=stationservice.station.line.pk)
		for pref in prefs:
			lineservice.pref_codes.add(pref)
		for line in lines:
			lineservice.line.add(line)
		return redirect('ekimeimysql1:railwaysearch')

	context = {
		'lineservice': lineservice,
		'lines': lines,
		'last_code': last_code,
		'formset': formset
	}

	return render(request, 'ekimeimysql1/stationserviceregister.html', context)

def Stationservicegroupcodeset(request):
	if 'csv' in request.FILES:
		updatestationservices = []
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		i = 0
		for line in csv_file:
			if i != 0:
				stationservice = StationService.objects.get(station_service=line[0])
				stationservice.station_service_group_code = line[1]
				updatestationservices.append(stationservice)
			else:
				i+=1
		StationService.objects.bulk_update(updatestationservices, fields=[
			'station_service_group_code'
		])

		return render(request, 'ekimeimysql1/upload.html')

	else:
		return render(request, 'ekimeimysql1/upload.html')



def detail_movie(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	parts = Part.objects.filter(movie=movie).order_by('part_num')
	songs = Song.objects.none()
	for part in parts:
		part_songs = part.part_song.all()
		for song in part_songs:
			songs |= Song.objects.filter(id=song.pk)

	context = {
		'movie': movie,
		'parts': parts,
		'songs': songs
	}

	return render(request, 'ekimeimysql1/detail.html', context)

class OnlyYouMixin(UserPassesTestMixin):
	raise_exception = True

	def test_func(self):
		user = self.request.user
		return user.is_superuser

class MovieRegisterView(OnlyYouMixin, generic.CreateView):
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
		querysetzero = Part.objects.filter(movie=main_id, part_num=0)
		queryset = Part.objects.filter(movie=main_id, part_num=1)
		if (request.POST['single-part-boolean'] == "true") and querysetzero.first():
			name = movie.channel.channel_main_name
			if name == None:
				name, created = Name.objects.get_or_create(name=movie.channel.name, creator=movie.channel.creator)
			querysetzero.first().participant.add(name)
			songs = movie.song.all()
			for song in songs:
				querysetzero.first().part_song.add(song)
		if querysetzero.first():
			return redirect('ekimeimysql1:station_edit', main_id=main_id, part_num=0)
		elif queryset.first():
			return redirect('ekimeimysql1:station_edit', main_id=main_id, part_num=1)
		else:
			return redirect('ekimeimysql1:detail', main_id=main_id)


	names = Name.objects.all()
	songs = Song.objects.all()

	context = {
		'movie': movie,
		'form': form,
		'formset': formset,
		'names': names,
		'songs': songs
	}

	return render(request, 'ekimeimysql1/part_edit.html', context)

def movie_part_station_edit(request, main_id, part_num):
	part = get_object_or_404(Part, movie=main_id, part_num=part_num)
	part_form = forms.PartEditForm(request.POST or None, instance=part)
	formset = forms.StationInMovieEditFormset(request.POST or None, instance=part)
	if request.method == 'POST' and part_form.is_valid() and formset.is_valid():
		part_form.save()
		stations = StationInMovie.objects.filter(movie_part=part)
		stations.delete()
		lines = LineInMovie.objects.filter(movie_part=part)
		lines.delete()
		formset.save()

		stations = StationInMovie.objects.filter(movie_part=part)
		lines = LineService.objects.none()
		lineinmovies = []
		for station in stations:
			lines |= LineService.objects.filter(pk=station.station_service.line_service.pk)
		for line in lines:
			lineinmovie = LineInMovie(movie_part=part, line_service=line)
			lineinmovies.append(lineinmovie)
		LineInMovie.objects.bulk_create(lineinmovies)

		queryset = Part.objects.filter(movie=main_id, part_num=part_num+1)
		if queryset.first() is None:
			return redirect('ekimeimysql1:detail', main_id=main_id)
		else:
			return redirect('ekimeimysql1:station_edit', main_id=main_id, part_num=part_num+1)

	context = {
		'part': part,
		'part_form': part_form,
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
		line = station.line
		pref = station.pref_code
		line.pref_codes.add(pref)

	return render(request, 'ekimeimysql1/lineprefset.html')

def lineserviceprefset(request):
	stationservices = StationService.objects.all()
	for stationservice in stationservices:
		line = stationservice.line_service
		pref = stationservice.station.pref_code
		line.pref_codes.add(pref)

	return render(request, 'ekimeimysql1/lineprefset.html')

def lineservicelineset(request):
	stationservices = StationService.objects.all()
	for stationservice in stationservices:
		lineservice = stationservice.line_service
		line = stationservice.station.line
		lineservice.line.add(line)
	return a

class StationViewSet(generics.ListAPIView):
	serializer_class = serializer.StationSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['line_pk']
		return Station.objects.filter(line=query_my_name)

class StationServiceViewSet(generics.ListAPIView):
	serializer_class = serializer.StationServiceSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['line_service_pk']
		return StationService.objects.filter(line_service=query_my_name)

class LineServiceViewSet(generics.ListAPIView):
	serializer_class = serializer.LineServiceSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['pref_code']
		return LineService.objects.filter(pref_codes__pref_code=query_my_name)

class StationServiceSearchViewSet(generics.ListAPIView):
	serializer_class = serializer.StationServiceSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['words']
		return StationService.objects.filter(station_name__contains=query_my_name)

class TransferViewSet(generics.ListAPIView):
	serializer_class = serializer.LineServiceSerializer
	def get_queryset(self):
		stationservice = StationService.objects.get(pk=self.kwargs['station_service_pk'])
		stations = Station.objects.filter(station_group_code=stationservice.station.station_group_code)
		lines = []
		for station in stations:
			stationservices = StationService.objects.filter(station=station)
			for stationservice in stationservices:
				lines.append(stationservice.line_service)
		return lines

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